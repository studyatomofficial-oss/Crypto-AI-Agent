import sqlite3
from pathlib import Path


class Database:
    def __init__(self, db_path: str = "database/crypto_agent.db") -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self._initialize()

    def _initialize(self) -> None:
        self.conn.execute("SELECT 1")
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
