# Changelog

## Version 1.0.0 — 07 July 2026

Initial production release.

### Features

- **Bybit Scanner** — Fetches all USDT perpetual futures contracts
- **Universe Filter** — Restricts to 3x–10x maximum leverage contracts
- **Crash Analysis** — Measures decline from 90-day high
- **Accumulation Detection** — Counts consecutive days consolidating at bottom
- **Compression Analysis** — Measures tightness of 30-day trading range
- **Bottom Stability** — Calculates average distance from 30-day low
- **Recovery Analysis** — Measures how much of the crash is already recovered
- **Weighted Sleeping Score** — Composite 0–100 score (crash 40%, accumulation 25%, compression 20%, stability 10%, recovery 5%)
- **Top 25 Ranking** — Coins ranked descending by sleeping score
- **CSV Export** — Timestamped output with Scan ID and Strategy Version
- **Scan History Engine** — Permanent archive in `output/history/`
- **Watchlist Change Detector** — New entries, rank movers, removed coins
- **Telegram Notifications** — Sends scan summary + latest.csv after each scan
- **API Retry Logic** — Automatic 3-attempt retry on network failures
- **Data Validation** — Skips coins with invalid or missing candle data
- **Error Logging** — All failures logged to `output/logs/app.log`
- **Live Progress Bar** — Real-time scanning progress display
- **Scan Summary** — Prints universe size, top results, score stats, duration
- **Startup Banner** — Displays strategy name, version, exchange, and universe
