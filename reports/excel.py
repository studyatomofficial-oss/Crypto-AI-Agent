import pandas as pd
from pathlib import Path


class ExcelReporter:
    def export(self, data: list[dict], path: str = "output/excel/signals.xlsx") -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        df = pd.DataFrame(data)
        df.to_excel(path, index=False)
