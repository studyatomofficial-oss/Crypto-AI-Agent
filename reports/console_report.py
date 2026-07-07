class ConsoleReport:
    def show(self, results) -> None:
        print()
        print("=" * 100)
        print("SLEEPING GIANTS SCANNER")
        print("=" * 100)
        print()
        print(
            f"{'Rank':<6}"
            f"{'Symbol':<14}"
            f"{'Score':<8}"
            f"{'Reason':<65}"
        )
        print("-" * 100)
        for i, item in enumerate(results, start=1):
            print(
                f"{i:<6}"
                f"{item.symbol:<14}"
                f"{item.score:>6.1f}  "
                f"{item.reason:<65}"
            )
        print()
