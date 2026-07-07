from pathlib import Path
from datetime import datetime
import pandas as pd


class CsvReport:

    def save(self, opportunities):
        
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = (
            "sleeping_giants_"
            + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            + ".csv"
        )

        filepath = output_dir / filename

        rows = []

        for rank, coin in enumerate(opportunities, start=1):

            rows.append({

                "Rank": rank,

                "Symbol": coin.symbol,

                "Sleeping Score": round(coin.score, 2),

                "Crash %": round(coin.crash_pct, 2),

                "Accumulation Days": coin.accumulation_days,

                "Compression %": round(
                    coin.compression_percent,
                    2,
                ),

                "Bottom Stability %": round(
                    coin.bottom_stability_percent,
                    2,
                ),

                "Recovery %": round(
                    coin.recovery_percent,
                    2,
                ),

                "Current Price": coin.current_price,

                "30D Low": coin.low_30d,

                "Scan Time": scan_time,

            })

        df = pd.DataFrame(rows)

        df.to_csv(filepath, index=False)

        return filepath.name
