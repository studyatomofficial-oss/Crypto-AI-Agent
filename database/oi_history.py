import sqlite3
from datetime import date, datetime, timedelta


class OIHistoryRepository:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        self._initialize()

    def _initialize(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS oi_history (
                symbol TEXT NOT NULL,
                snapshot_date TEXT NOT NULL,
                open_interest REAL NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                PRIMARY KEY (symbol, snapshot_date)
            )
            """
        )
        self.conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_oi_history_symbol_date
            ON oi_history(symbol, snapshot_date)
            """
        )
        self.conn.commit()

    def upsert_daily(self, symbol: str, open_interest: float, as_of_date: date | None = None) -> None:
        snapshot_day = as_of_date or date.today()
        now = datetime.utcnow().isoformat()
        self.conn.execute(
            """
            INSERT INTO oi_history(symbol, snapshot_date, open_interest, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(symbol, snapshot_date)
            DO UPDATE SET
                open_interest = excluded.open_interest,
                updated_at = excluded.updated_at
            """,
            (symbol, snapshot_day.isoformat(), open_interest, now, now),
        )
        self.conn.commit()

    def get_baseline_open_interest(self, symbol: str, days_back: int = 30, as_of_date: date | None = None) -> float | None:
        snapshot_day = as_of_date or date.today()
        target_day = snapshot_day - timedelta(days=days_back)
        row = self.conn.execute(
            """
            SELECT open_interest
            FROM oi_history
            WHERE symbol = ?
              AND snapshot_date <= ?
            ORDER BY snapshot_date DESC
            LIMIT 1
            """,
            (symbol, target_day.isoformat()),
        ).fetchone()
        if row is None:
            return None
        return float(row[0])

    def compute_30d_change(self, symbol: str, current_open_interest: float, as_of_date: date | None = None) -> float:
        baseline = self.get_baseline_open_interest(symbol, days_back=30, as_of_date=as_of_date)
        if baseline is None or baseline <= 0:
            return 0.0
        return ((current_open_interest - baseline) / baseline) * 100.0
