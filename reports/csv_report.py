import csv
from pathlib import Path


class CSVReporter:
    def report(self, opportunities, path: str = "output/csv/scans.csv") -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["symbol", "score", "distance"])
            for opportunity in opportunities:
                writer.writerow([opportunity.symbol, opportunity.score, opportunity.distance_pct])
