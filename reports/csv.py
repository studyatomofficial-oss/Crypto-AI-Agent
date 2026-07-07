import csv
from pathlib import Path


class CSVReporter:
    def export(self, data: list[dict], path: str = "output/csv/signals.csv") -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=data[0].keys() if data else ["symbol", "score"])
            writer.writeheader()
            writer.writerows(data)
