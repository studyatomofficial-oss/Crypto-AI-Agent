class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 115)
        print("CRYPTO OPPORTUNITY SCANNER  —  Sleeping Coins")
        print("=" * 115)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<18}"
            f"{'Crash':<10}"
            f"{'Accum Days':<12}"
            f"{'Compr%':<8}"
            f"{'Bottom%':<10}"
            f"{'Score':<10}"
        )
        print("-" * 115)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<18}"
                f"{item.crash_pct:>7.1f}%  "
                f"{item.accumulation_days:>8}    "
                f"{item.compression_percent:>5.1f}%  "
                f"{item.bottom_stability_percent:>7.1f}%  "
                f"{item.score:>8.0f}"
            )
        print()
