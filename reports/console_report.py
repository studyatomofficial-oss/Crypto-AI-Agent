class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 130)
        print("CRYPTO OPPORTUNITY SCANNER  —  Sleeping Coins")
        print("=" * 130)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<18}"
            f"{'Crash':<10}"
            f"{'Accum Days':<12}"
            f"{'Compr%':<8}"
            f"{'Recovery%':<10}"
            f"{'RecoverySc':<12}"
            f"{'Score':<10}"
        )
        print("-" * 130)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<18}"
                f"{item.crash_pct:>7.1f}%  "
                f"{item.accumulation_days:>8}    "
                f"{item.compression_percent:>5.1f}%  "
                f"{item.recovery_percent:>7.1f}%  "
                f"{item.recovery_score:>10.0f}  "
                f"{item.score:>8.0f}"
            )
        print()
