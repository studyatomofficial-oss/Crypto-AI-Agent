class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 90)
        print("CRYPTO OPPORTUNITY SCANNER")
        print("=" * 90)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<18}"
            f"{'Distance':<12}"
            f"{'Volume':<14}"
            f"{'Open Interest':<16}"
            f"{'Funding':<12}"
            f"{'Score':<8}"
        )
        print("-" * 90)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<18}"
                f"{item.distance_pct:>8.2f}%   "
                f"{item.volume_24h / 1_000_000:>8.2f}M     "
                f"{item.open_interest / 1_000_000:>8.2f}M       "
                f"{item.funding_rate:>10.5f}  "
                f"{item.score:>8.2f}"
            )
        print()
