from datetime import date, timedelta
import sqlite3

from database.oi_history import OIHistoryRepository
from models.candle import Candle
from models.market_snapshot import MarketSnapshot
from scanner.accumulation import AccumulationAnalyzer
from scanner.psychology_scorer import PsychologyScorer


def test_compression_percent_uses_midpoint_normalization() -> None:
    snapshot = MarketSnapshot(symbol="TESTUSDT", current_price=75.0, low_30d=0.0)
    candles = [
        Candle(timestamp=1, open=60.0, high=100.0, low=50.0, close=75.0, volume=1.0, turnover=1.0),
        Candle(timestamp=2, open=70.0, high=90.0, low=55.0, close=80.0, volume=1.0, turnover=1.0),
    ]

    AccumulationAnalyzer().analyze(snapshot, candles)

    assert round(snapshot.compression_percent, 2) == 66.67


def test_oi_history_average_returns_recent_window_average() -> None:
    conn = sqlite3.connect(":memory:")
    repo = OIHistoryRepository(conn)
    today = date(2026, 7, 10)

    repo.upsert_daily("BTCUSDT", 100.0, today - timedelta(days=3))
    repo.upsert_daily("BTCUSDT", 120.0, today - timedelta(days=2))
    repo.upsert_daily("BTCUSDT", 140.0, today - timedelta(days=1))

    assert repo.get_average_open_interest("BTCUSDT", 7, today) == 120.0


def test_open_interest_score_uses_average_deviation_instead_of_defaulting_to_five() -> None:
    snapshot = MarketSnapshot(symbol="BTCUSDT", current_price=100.0, low_30d=90.0)
    snapshot.oi_avg_7d = 100.0
    snapshot.oi_avg_30d = 120.0
    snapshot.oi_vs_7d_avg = -20.0
    snapshot.oi_vs_30d_avg = -25.0

    PsychologyScorer().score_open_interest(snapshot)

    assert snapshot.oi_score == 7


def test_open_interest_score_is_zero_without_history() -> None:
    snapshot = MarketSnapshot(symbol="BTCUSDT", current_price=100.0, low_30d=90.0)

    PsychologyScorer().score_open_interest(snapshot)

    assert snapshot.oi_score == 0


def test_false_break_score_is_graded_for_medium_quality_reclaim() -> None:
    snapshot = MarketSnapshot(symbol="BTCUSDT", current_price=100.0, low_30d=90.0)
    snapshot.candles = [
        Candle(timestamp=1, open=103.0, high=105.0, low=100.0, close=102.0, volume=1.0, turnover=1.0),
        Candle(timestamp=2, open=102.0, high=104.0, low=101.0, close=103.0, volume=1.0, turnover=1.0),
        Candle(timestamp=3, open=101.0, high=103.0, low=100.5, close=101.5, volume=1.0, turnover=1.0),
        Candle(timestamp=4, open=100.0, high=101.0, low=99.2, close=99.7, volume=1.0, turnover=1.0),
        Candle(timestamp=5, open=99.6, high=100.4, low=99.1, close=100.1, volume=1.0, turnover=1.0),
        Candle(timestamp=6, open=100.1, high=100.8, low=99.4, close=100.6, volume=1.0, turnover=1.0),
        Candle(timestamp=7, open=100.4, high=101.0, low=99.8, close=100.7, volume=1.0, turnover=1.0),
        Candle(timestamp=8, open=100.5, high=101.2, low=99.9, close=100.8, volume=1.0, turnover=1.0),
        Candle(timestamp=9, open=100.2, high=101.0, low=99.7, close=100.4, volume=1.0, turnover=1.0),
        Candle(timestamp=10, open=100.0, high=100.9, low=99.6, close=100.2, volume=1.0, turnover=1.0),
        Candle(timestamp=11, open=100.1, high=101.1, low=99.8, close=100.5, volume=1.0, turnover=1.0),
        Candle(timestamp=12, open=100.2, high=101.0, low=99.7, close=100.3, volume=1.0, turnover=1.0),
        Candle(timestamp=13, open=100.0, high=100.8, low=99.6, close=100.1, volume=1.0, turnover=1.0),
        Candle(timestamp=14, open=99.9, high=100.7, low=99.5, close=100.0, volume=1.0, turnover=1.0),
        Candle(timestamp=15, open=99.8, high=100.6, low=99.4, close=99.9, volume=1.0, turnover=1.0),
        Candle(timestamp=16, open=99.7, high=100.3, low=98.0, close=99.3, volume=1.0, turnover=1.0),
        Candle(timestamp=17, open=99.4, high=100.5, low=99.0, close=100.2, volume=1.0, turnover=1.0),
        Candle(timestamp=18, open=100.2, high=101.1, low=99.8, close=100.7, volume=1.0, turnover=1.0),
    ]

    PsychologyScorer().score_false_break(snapshot)

    assert snapshot.false_break_detected is True
    assert snapshot.false_break_score == 5