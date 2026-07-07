class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 120)
        print("CRYPTO OPPORTUNITY SCANNER  —  Sleeping Coins")
        print("=" * 120)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<18}"
            f"{'Crash':<10}"
            f"{'Days':<8}"
            f"{'Compr%':<8}"
            f"{'AvgDist%':<10}"
            f"{'BottomSc':<10}"
            f"{'SleepSc':<10}"
        )
        print("-" * 120)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<18}"
                f"{item.crash_pct:>7.1f}%  "
                f"{item.days_near_bottom:>5}  "
                f"{item.compression_percent:>5.1f}%  "
                f"{item.bottom_stability_percent:>7.1f}%  "
                f"{item.bottom_stability_score:>8.0f}  "
                f"{item.score:>8.0f}"
            )
        print()
