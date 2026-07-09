class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 140)
        print("SLEEPING GIANTS SCANNER")
        print("=" * 140)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<14}"
            f"{'Sleeping':<10}"
            f"{'Funding':<9}"
            f"{'Psych':<8}"
            f"{'Final':<8}"
            f"{'Reason':<65}"
        )
        print("-" * 140)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<14}"
                f"{item.score:>8.1f}  "
                f"{item.funding_score:>7.1f}  "
                f"{item.psychology_score:>6.1f}  "
                f"{item.final_score:>6.1f}  "
                f"{item.reason:<65}"
            )
        print()
