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
    min_leverage: int = 4
    max_leverage: int = 10
    lookback_days: int = 30
    max_distance_from_low: float = 5.0
    min_volume_24h: float = 5_000_000
    min_open_interest: float = 1_000_000
    max_results: int = 20


settings = Settings()

MIN_LEVERAGE = settings.min_leverage
MAX_LEVERAGE = settings.max_leverage
LOOKBACK_DAYS = settings.lookback_days
MAX_DISTANCE_FROM_LOW = settings.max_distance_from_low
MIN_VOLUME_24H = settings.min_volume_24h
MIN_OPEN_INTEREST = settings.min_open_interest
MAX_RESULTS = settings.max_results
