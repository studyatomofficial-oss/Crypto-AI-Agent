import csv
import os
from datetime import datetime


class CSVExporter:
    @staticmethod
    def export(results, output_dir: str = "output") -> str:
        """Export scanning results to CSV file."""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/sleeping_giants_{timestamp}.csv"
        
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "Rank",
                "Symbol",
                "Score",
                "Crash%",
                "Consecutive Bottom Days",
                "Compression%",
                "Bottom Stability%",
                "Recovery%",
                "Current Price",
                "30D Low",
                "Reason"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for i, item in enumerate(results, start=1):
                writer.writerow({
                    "Rank": i,
                    "Symbol": item.symbol,
                    "Score": f"{item.score:.1f}",
                    "Crash%": f"{item.crash_pct:.1f}%",
                    "Consecutive Bottom Days": item.accumulation_days,
                    "Compression%": f"{item.compression_percent:.1f}%",
                    "Bottom Stability%": f"{item.bottom_stability_percent:.1f}%",
                    "Recovery%": f"{item.recovery_percent:.1f}%",
                    "Current Price": f"{item.current_price:.8f}",
                    "30D Low": f"{item.low_30d:.8f}",
                    "Reason": item.reason
                })
        
        return filename
