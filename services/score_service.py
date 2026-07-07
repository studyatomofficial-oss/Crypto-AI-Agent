class ScoreService:
    def rank(self, data: list[dict]) -> list[dict]:
        return sorted(data, key=lambda item: item.get("score", 0), reverse=True)
