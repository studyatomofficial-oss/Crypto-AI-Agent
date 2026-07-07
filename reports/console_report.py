class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 85)
        print("CRYPTO OPPORTUNITY SCANNER  —  Sleeping Coins")
        print("=" * 85)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<18}"
            f"{'Crash':<10}"
            f"{'Crash Score':<15}"
            f"{'Sleeping Score':<15}"
        )
        print("-" * 85)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<18}"
                f"{item.crash_pct:>7.1f}%   "
                f"{item.score:>10.0f}      "
                f"{item.score:>10.0f}"
            )
        print()
