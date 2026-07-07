class Ranker:
    def rank(self, snapshots):
        return sorted(snapshots, key=lambda item: item.score, reverse=True)
