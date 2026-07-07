class TelegramReporter:
    def __init__(self, bot_token: str = "") -> None:
        self.bot_token = bot_token

    def send_message(self, message: str) -> None:
        print(f"Telegram message would be sent: {message}")
