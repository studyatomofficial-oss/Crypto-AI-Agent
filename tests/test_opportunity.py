from models.market_snapshot import MarketSnapshot
from models.opportunity import Opportunity
from scanner.ranker import Ranker


def test_ranker_emits_opportunity_objects() -> None:
    snapshot = MarketSnapshot(
        symbol="BTCUSDT",
        current_price=100.0,
        low_30d=80.0,
        distance=2.0,
        volume_24h=10_000_000.0,
        funding_rate=0.0001,
        open_interest=2_000_000.0,
        score=9.5,
    )
    snapshot.is_qualified = True

    opportunities = Ranker().rank([snapshot])

    assert len(opportunities) == 1
    assert isinstance(opportunities[0], Opportunity)
    assert opportunities[0].symbol == "BTCUSDT"
    assert opportunities[0].distance_pct == 2.0
    assert opportunities[0].score == 9.5
