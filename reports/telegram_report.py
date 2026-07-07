class TelegramReporter:
    def report(self, opportunities) -> None:
        for opportunity in opportunities:
            print(f"Telegram: {opportunity.symbol} -> {opportunity.score}")
