class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 110)
        print("CRYPTO OPPORTUNITY SCANNER  —  Sleeping Coins")
        print("=" * 110)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<18}"
            f"{'Crash':<10}"
            f"{'Days@Bot':<10}"
            f"{'Crash Sc':<10}"
            f"{'Accum Sc':<10}"
            f"{'Sleeping Sc':<12}"
        )
        print("-" * 110)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<18}"
                f"{item.crash_pct:>7.1f}%   "
                f"{item.days_near_bottom:>6}    "
                f"{item.crash_score:>8.0f}  "
                f"{item.accumulation_score:>8.0f}  "
                f"{item.score:>8.0f}"
            )
        print()
