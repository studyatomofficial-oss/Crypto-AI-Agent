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
            f"{'Crash%':<10}"
            f"{'Consecutive Bot Days':<22}"
            f"{'Compr%':<10}"
            f"{'Recovery%':<12}"
            f"{'Score':<10}"
        )
        print("-" * 110)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<18}"
                f"{item.crash_pct:>7.1f}%  "
                f"{item.accumulation_days:>18}     "
                f"{item.compression_percent:>7.1f}%  "
                f"{item.recovery_percent:>9.1f}%  "
                f"{item.score:>8.1f}"
            )
        print()
