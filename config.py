import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    # API
    BYBIT_BASE_URL: str = "https://api.bybit.com"
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    BYBIT_API_KEY: str = os.getenv("BYBIT_API_KEY", "")
    BYBIT_API_SECRET: str = os.getenv("BYBIT_API_SECRET", "")
    BYBIT_TESTNET: bool = os.getenv("BYBIT_TESTNET", "false").lower() == "true"

    # Universe
    MIN_LEVERAGE: int = 4
    MAX_LEVERAGE: int = 10

    # Scanner
    LOOKBACK_DAYS: int = 30
    LOOKBACK_90D: int = 90
    MAX_DISTANCE_FROM_LOW: float = 5.0

    # Liquidity
    MIN_VOLUME_24H: float = 5_000_000
    MIN_OPEN_INTEREST: float = 1_000_000

    # Output
    MAX_RESULTS: int = 20


settings = Settings()
