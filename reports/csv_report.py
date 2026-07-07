import csv
from pathlib import Path


class CSVReporter:
    def report(self, opportunities, path: str = "output/opportunities.csv") -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["rank", "symbol", "distance", "score"])
            for index, opportunity in enumerate(opportunities, start=1):
                writer.writerow([index, opportunity.symbol, f"{opportunity.distance_pct:.2f}%", f"{opportunity.score:.1f}"])
