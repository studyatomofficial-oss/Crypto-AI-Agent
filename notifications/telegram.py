from pathlib import Path
from telegram import Bot
import asyncio


class TelegramNotifier:

    def __init__(
        self,
        token: str,
        chat_id: str,
    ):
        self.bot = Bot(token=token)
        self.chat_id = chat_id

    async def send_message(
        self,
        message: str,
    ):
        await self.bot.send_message(
            chat_id=self.chat_id,
            text=message,
        )

    async def send_document(
        self,
        filepath: str,
    ):
        with open(filepath, "rb") as file:
            await self.bot.send_document(
                chat_id=self.chat_id,
                document=file,
            )

    async def send_report(
        self,
        message: str,
        csv_file: str,
    ):
        await self.send_message(message)
        if Path(csv_file).exists():
            await self.send_document(csv_file)

    def notify(
        self,
        message: str,
        csv_file: str,
    ):
        asyncio.run(
            self.send_report(
                message,
                csv_file,
            )
        )
