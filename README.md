# Crypto AI Agent — Sleeping Giants Scanner

A quantitative cryptocurrency scanner that identifies **"Sleeping Giant"** perpetual futures contracts on Bybit before major market participation begins.

The scanner analyzes every eligible 3x–10x leverage perpetual contract, scores each coin using a proprietary multi-factor model, ranks the strongest opportunities, exports reports, maintains a scan history database, and delivers results directly to Telegram.

---

## Features

- Bybit USDT Perpetual Market Scanner
- 3x–10x Maximum Leverage Universe Filter
- 90-Day Crash Analysis
- Consecutive Bottom Accumulation Detection
- Compression (Range) Analysis
- Bottom Stability Analysis
- Recovery Analysis
- Weighted Sleeping Score (0–100)
- Top 25 Opportunity Ranking
- CSV Export with Scan ID and Strategy Version
- Historical Scan Archive (`output/history/`)
- Watchlist Change Detection (new entries, rank movers, removed)
- Telegram Notifications with CSV attachment
- Automatic API Retry and Error Handling
- Failure Logging to `output/logs/app.log`

---

## Strategy

The objective is **not** to find coins that are already pumping.

Instead, the scanner identifies coins that:

- Experienced a significant decline from their 90-day high
- Remained near the bottom for an extended period
- Entered a low-volatility accumulation phase
- Have not yet recovered significantly
- Still belong to the 3x–10x leverage perpetual universe

The goal is to enter **before** broad market participation begins.

### Scoring Weights

| Metric             | Weight | Description                              |
|--------------------|--------|------------------------------------------|
| Crash %            | 40%    | Size of decline from 90-day high         |
| Accumulation Days  | 25%    | Consecutive days consolidating at bottom |
| Compression %      | 20%    | Tightness of 30-day trading range        |
| Bottom Stability   | 10%    | Average distance from 30-day low         |
| Recovery %         | 5%     | How much of the crash is already recovered |

---

## Architecture

```
               Bybit Public API
                      │
                      ▼
             Market Data Collector
                      │
                      ▼
             Sleeping Giant Scanner
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Ranking Engine   CSV Export     History Engine
      │               │                │
      └───────────────┼────────────────┘
                      ▼
              Telegram Notification
                      ▼
                 Mobile Device
```

---

## Project Structure

```
Crypto-AI-Agent/
│
├── api/                   # Bybit API client
├── models/                # Data models (MarketSnapshot, Opportunity, Candle)
├── scanner/               # Core scan logic (crash, accumulation, sleep, scoring, ranking)
├── services/              # Market service (candles, tickers, OI)
├── reports/               # Console report, CSV export, change detector
├── notifications/         # Telegram notifier
├── utils/                 # Progress bar, retry decorator, logger
├── tests/                 # pytest test suite
│
├── output/
│   ├── latest.csv         # Always the most recent scan
│   ├── history/           # Timestamped scan archive
│   └── logs/              # app.log for error tracking
│
├── config.py              # Runtime settings (loaded from .env)
├── strategy.py            # Frozen strategy constants (v1.0.0)
├── main.py                # Entry point
├── requirements.txt
├── Install.bat            # First-time setup (Windows)
├── Run Scanner.bat        # Daily scan launcher (Windows)
├── Open Output Folder.bat # Shortcut to output directory
└── README.md
```

---

## Installation

```bash
git clone <repository>
cd Crypto-AI-Agent

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root:

```env
# Bybit API (optional — scanner uses public endpoints only)
BYBIT_API_KEY=
BYBIT_API_SECRET=

# Telegram (optional)
ENABLE_TELEGRAM=True
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

To get your Telegram credentials:
1. Create a bot via [@BotFather](https://t.me/BotFather) and copy the token
2. Get your chat ID by messaging [@userinfobot](https://t.me/userinfobot)

---

## Run

### Windows (Double-click)

**First time setup:**

```
Double-click: Install.bat
```

This creates the virtual environment and installs all dependencies.

**Every day:**

```
Double-click: Run Scanner.bat
```

No terminal. No VS Code. No Python knowledge required.

**Open results:**

```
Double-click: Open Output Folder.bat
```

### Command Line

```bash
python main.py
```

---

## Sample Output

```
============================================================
Sleeping Giants
Version     : 1.0.0
Strategy    : Crash -> Accumulation -> Recovery
Exchange    : Bybit USDT Perpetual
Universe    : 3x-10x Leverage Contracts
============================================================

Cached 720 tickers.

>> Starting Sleeping Giants Scan...
Eligible Contracts : 47

Scanning: [........................................] 100.00% (47/47)

>> Scan Complete!

====================================================================================================
SLEEPING GIANTS SCANNER
====================================================================================================

Rank  Symbol        Score   Reason
----------------------------------------------------------------------------------------------------
1     TACUSDT         46.1  93% crash - 2 bottom days - 1394% range - 0.7% recovery
2     ESPORTSUSDT     45.0  98% crash - 0 bottom days - 1666% range - 0.0% recovery
...

=======================================================
SCAN SUMMARY
=======================================================

Universe               : 47
Top Results            : 25
Strategy               : 1.0.0

Scan ID                : 20260707_214507
Scan Duration          : 21.94 sec

Latest CSV             : output/latest.csv
History CSV            : output/history/sleeping_giants_2026-07-07_21-45-07.csv
=======================================================

Telegram notification sent.

============================================================
WATCHLIST CHANGES
============================================================

>> New Entries (1)

   + TACUSDT (#1)

------------------------------------------------------------

>> Biggest Rank Improvements

   PUMPBTCUSDT     #14 -> #12
   RONINUSDT       #9 -> #8

------------------------------------------------------------

>> Biggest Rank Drops

   PROMPTUSDT      #8 -> #9

------------------------------------------------------------

>> Removed (1)

   - VELVETUSDT

============================================================
```

---

## Telegram Notification

Every successful scan automatically:

- Sends a text summary (top results, highest/lowest score, scan duration)
- Attaches `latest.csv` directly to the chat

Set `ENABLE_TELEGRAM=False` in `.env` to disable without changing any code.

---

## Output Files

| File | Description |
|------|-------------|
| `output/latest.csv` | Most recent scan, overwritten each run |
| `output/history/*.csv` | Permanent archive of every scan |
| `output/logs/app.log` | Error log for failed symbols and API issues |

Each CSV row contains: `Scan ID`, `Rank`, `Symbol`, `Sleeping Score`, `Crash %`, `Accumulation Days`, `Compression %`, `Bottom Stability %`, `Recovery %`, `Current Price`, `30D Low`, `Scan Time`, `Strategy Version`.

---

## Roadmap

### Version 1.0 (Current)
- [x] Bybit perpetual scanner
- [x] 5-metric weighted scoring model
- [x] Top 25 ranking
- [x] CSV export with scan history
- [x] Watchlist change detection
- [x] Telegram notifications
- [x] Retry logic and error handling

### Version 2.0 (Planned)
- [ ] Historical backtesting engine
- [ ] Portfolio tracking
- [ ] Daily automated scheduler
- [ ] Web dashboard
- [ ] Performance analytics
- [ ] Multi-exchange support

---

## Disclaimer

This project is intended for **educational and research purposes only**.

It does not provide financial advice. Cryptocurrency trading involves significant risk of loss. Always perform your own research before making any trading decisions.

---

## License

MIT License

