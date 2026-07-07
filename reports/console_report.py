class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 100)
        print("CRYPTO OPPORTUNITY SCANNER  —  Sleeping Coins")
        print("=" * 100)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<18}"
            f"{'Crash':<10}"
            f"{'30D Range':<12}"
            f"{'Position':<12}"
            f"{'Days@Bot':<10}"
            f"{'ADR':<8}"
            f"{'VolDry':<10}"
            f"{'Score':<8}"
        )
        print("-" * 100)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<18}"
                f"{item.crash_pct:>7.1f}%   "
                f"{item.range_30d:>8.1f}%   "
                f"{item.position:>8.1f}%   "
                f"{item.days_near_bottom:>6}    "
                f"{item.adr:>5.1f}%  "
                f"{item.vol_dryup:>6.0f}%   "
                f"{item.score:>8.1f}"
            )
        print()
