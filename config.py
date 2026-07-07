from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class Settings:
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    bybit_api_key: str = os.getenv("BYBIT_API_KEY", "")
    bybit_api_secret: str = os.getenv("BYBIT_API_SECRET", "")
    bybit_testnet: bool = os.getenv("BYBIT_TESTNET", "false").lower() == "true"


settings = Settings()
