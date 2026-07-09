from pathlib import Path
import pandas as pd


class RollingReport:
    def summarize(self):
        try:
            history_files = sorted(Path("output/history").glob("sleeping_giants_*.csv"))
            if len(history_files) < 2:
                return None

            latest_file = history_files[-1]
            latest_name = latest_file.name

            # Keep the rolling view scoped to the same day as the latest scan.
            day_key = latest_name.replace("sleeping_giants_", "")[:10]
            daily_files = [f for f in history_files if f.name.startswith(f"sleeping_giants_{day_key}_")]
            if len(daily_files) < 2:
                daily_files = history_files[-2:]

            daily_frames = [pd.read_csv(path) for path in daily_files]
            previous = daily_frames[-2]
            current = daily_frames[-1]

            # Daily Top-25 overlap across all scans in the selected rolling window.
            symbol_sets = [set(frame["Symbol"].astype(str)) for frame in daily_frames if "Symbol" in frame.columns]
            overlap_count = len(set.intersection(*symbol_sets)) if symbol_sets else 0

            old_rank = {
                row["Symbol"]: int(row["Rank"])
                for _, row in previous.iterrows()
            }
            new_rank = {
                row["Symbol"]: int(row["Rank"])
                for _, row in current.iterrows()
            }

            movers = []
            for symbol, rank in new_rank.items():
                if symbol in old_rank:
                    delta = old_rank[symbol] - rank
                    movers.append((symbol, delta, old_rank[symbol], rank))

            movers.sort(key=lambda item: abs(item[1]), reverse=True)
            biggest_movers = [item for item in movers if item[1] != 0][:5]

            # Average score contribution across the rolling daily window.
            combined = pd.concat(daily_frames, ignore_index=True)
            score_columns = [
                "Funding Score",
                "OI Score",
                "Crowd Score",
                "Base Score",
                "Psychology Score",
            ]
            for column in score_columns:
                if column not in combined.columns:
                    combined[column] = 0.0

            averages = {
                "funding": float(combined["Funding Score"].mean()),
                "oi": float(combined["OI Score"].mean()),
                "crowd": float(combined["Crowd Score"].mean()),
                "base": float(combined["Base Score"].mean()),
                "psych": float(combined["Psychology Score"].mean()),
            }

            return {
                "day_key": day_key,
                "latest_file": latest_name,
                "scan_id": str(current.get("Scan ID", pd.Series([""])).iloc[0]) if "Scan ID" in current.columns else "",
                "scan_time": str(current.get("Scan Time", pd.Series([""])).iloc[0]) if "Scan Time" in current.columns else "",
                "window_size": len(daily_files),
                "overlap_count": overlap_count,
                "biggest_movers": biggest_movers,
                "averages": averages,
            }
        except Exception:
            return None

    def report(self, summary):
        if not summary:
            return

        print()
        print("=" * 60)
        print("ROLLING PSYCHOLOGY SUMMARY")
        print("=" * 60)
        print()
        print(f"Day                     : {summary['day_key']}")
        print(f"Scans In Window         : {summary['window_size']}")
        print(f"Daily Top 25 Overlap    : {summary['overlap_count']}/25")
        print()

        movers = summary["biggest_movers"]
        print(">> Biggest Movers (Last Two Scans)")
        print()
        if not movers:
            print("   No comparable movers yet.")
        else:
            for symbol, delta, old_rank, new_rank in movers:
                direction = "up" if delta > 0 else "down" if delta < 0 else "flat"
                print(f"   {symbol:15} #{old_rank} -> #{new_rank} ({direction} {abs(delta)})")
        print()
        print("-" * 60)
        print()

        avg = summary["averages"]
        print(">> Average Psychology Contribution")
        print()
        print(f"   Funding              : {avg['funding']:.2f}")
        print(f"   OI                   : {avg['oi']:.2f}")
        print(f"   Crowd                : {avg['crowd']:.2f}")
        print(f"   Base                 : {avg['base']:.2f}")
        print(f"   Psych Total          : {avg['psych']:.2f}")
        print()
        print("=" * 60)

    def save_log(self, summary):
        if not summary:
            return

        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        log_path = output_dir / "rolling_summary.csv"

        movers_text = "; ".join(
            [
                f"{symbol}:{old_rank}->{new_rank}"
                for symbol, _, old_rank, new_rank in summary["biggest_movers"]
            ]
        )

        row = {
            "Day": summary["day_key"],
            "Scan ID": summary.get("scan_id", ""),
            "Scan Time": summary.get("scan_time", ""),
            "Latest History File": summary.get("latest_file", ""),
            "Scans In Window": summary["window_size"],
            "Daily Top 25 Overlap": summary["overlap_count"],
            "Avg Funding Score": round(summary["averages"]["funding"], 4),
            "Avg OI Score": round(summary["averages"]["oi"], 4),
            "Avg Crowd Score": round(summary["averages"]["crowd"], 4),
            "Avg Base Score": round(summary["averages"]["base"], 4),
            "Avg Psychology Score": round(summary["averages"]["psych"], 4),
            "Biggest Movers": movers_text,
        }

        if log_path.exists():
            existing = pd.read_csv(log_path)
            if "Scan ID" in existing.columns:
                if row["Scan ID"] and row["Scan ID"] in existing["Scan ID"].astype(str).values:
                    return
            updated = pd.concat([existing, pd.DataFrame([row])], ignore_index=True)
            updated.to_csv(log_path, index=False)
            return

        pd.DataFrame([row]).to_csv(log_path, index=False)
