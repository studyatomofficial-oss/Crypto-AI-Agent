class TelegramReporter:
    def report(self, snapshots) -> None:
        for snapshot in snapshots:
            print(f"Telegram: {snapshot.symbol} -> {snapshot.score}")
