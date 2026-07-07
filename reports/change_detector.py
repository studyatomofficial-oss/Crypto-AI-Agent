from pathlib import Path
import pandas as pd


class ChangeDetector:

    def compare(self):
        """Compare last two history files and return detected changes."""

        history = sorted(
            Path("output/history").glob("*.csv")
        )

        if len(history) < 2:
            return None

        previous = pd.read_csv(history[-2])
        current = pd.read_csv(history[-1])

        return self.detect(previous, current)

    def detect(self, previous, current):
        """Detect changes between previous and current scans."""

        old_rank = {
            row["Symbol"]: row["Rank"]
            for _, row in previous.iterrows()
        }

        new_rank = {
            row["Symbol"]: row["Rank"]
            for _, row in current.iterrows()
        }

        new_entries = []

        for symbol in new_rank:

            if symbol not in old_rank:

                new_entries.append(

                    (

                        symbol,

                        new_rank[symbol],

                    )

                )

        removed = []

        for symbol in old_rank:

            if symbol not in new_rank:

                removed.append(symbol)

        movers = []

        for symbol in new_rank:

            if symbol in old_rank:

                change = (

                    old_rank[symbol]

                    - new_rank[symbol]

                )

                movers.append(

                    (

                        symbol,

                        change,

                        old_rank[symbol],

                        new_rank[symbol],

                    )

                )

        movers.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return {
            "new_entries": new_entries,
            "removed": removed,
            "movers": movers,
        }

    def report(self, changes):
        """Print a formatted report of watchlist changes."""

        if not changes:
            return

        print()
        print("=" * 60)
        print("WATCHLIST CHANGES")
        print("=" * 60)
        print()

        new_entries = sorted(
            changes["new_entries"],
            key=lambda x: x[1]
        )

        if new_entries:
            print(f">> New Entries ({len(new_entries)})")
            print()
            for symbol, rank in new_entries:
                print(f"   + {symbol} (#{rank})")
            print()
            print("-" * 60)
            print()

        movers = changes["movers"]
        improvements = [m for m in movers if m[1] > 0]
        drops = [m for m in movers if m[1] < 0]

        if improvements:
            print(">> Biggest Rank Improvements")
            print()
            for symbol, change, old, new in improvements[:5]:
                print(
                    f"   {symbol:15} #{old} -> #{new}"
                )
            print()
            print("-" * 60)
            print()

        if drops:
            print(">> Biggest Rank Drops")
            print()
            for symbol, change, old, new in drops[:5]:
                print(
                    f"   {symbol:15} #{old} -> #{new}"
                )
            print()
            print("-" * 60)
            print()

        removed = changes["removed"]

        if removed:
            print(f">> Removed ({len(removed)})")
            print()
            for symbol in removed:
                print(f"   - {symbol}")
            print()

        print("=" * 60)
