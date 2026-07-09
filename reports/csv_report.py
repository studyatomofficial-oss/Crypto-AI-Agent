from pathlib import Path
from datetime import datetime
import pandas as pd
import strategy


class CsvReport:

    def save(self, opportunities):
        
        output_dir = Path("output")
        history_dir = output_dir / "history"
        output_dir.mkdir(exist_ok=True)
        history_dir.mkdir(exist_ok=True)

        scan_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        latest_file = output_dir / "latest.csv"
        
        history_filename = (
            "sleeping_giants_"
            + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            + ".csv"
        )
        
        history_file = history_dir / history_filename

        rows = []

        for rank, coin in enumerate(opportunities, start=1):

            rows.append({

                "Scan ID": scan_id,

                "Rank": rank,

                "Symbol": coin.symbol,

                "Sleeping Score": round(coin.score, 2),
                "Funding Score": round(coin.funding_score, 2),
                "OI Change 30D": round(coin.oi_change_30d, 2),
                "OI Score": round(coin.oi_score, 2),
                "Crowd Score": round(coin.crowd_score, 2),
                "Base Score": round(coin.base_score, 2),
                "False Break Score": round(coin.false_break_score, 2),
                "Recovery Failure Score": round(coin.recovery_failure_score, 2),
                "Psychology Score": round(coin.psychology_score, 2),
                "Final Score": round(coin.final_score, 2),

                "Crash %": round(coin.crash_pct, 2),

                "Accumulation Days": coin.accumulation_days,

                "Compression %": round(
                    coin.compression_percent,
                    2,
                ),

                "Bottom Stability %": round(
                    coin.bottom_stability_percent,
                    2,
                ),

                "Recovery %": round(
                    coin.recovery_percent,
                    2,
                ),

                "Current Price": coin.current_price,

                "30D Low": coin.low_30d,

                "Scan Time": scan_time,

                "Strategy Version": strategy.VERSION,

            })

        df = pd.DataFrame(rows)

        df.to_csv(latest_file, index=False)

        df.to_csv(history_file, index=False)

        return {
            "scan_id": scan_id,
            "latest": latest_file.name,
            "history": history_file.name,
        }
