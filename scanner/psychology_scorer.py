class PsychologyScorer:
    def score_funding(self, snapshot):
        funding = snapshot.funding_rate

        if funding <= 0:
            snapshot.funding_score = 10
        elif funding <= 0.002:
            snapshot.funding_score = 8
        elif funding <= 0.005:
            snapshot.funding_score = 5
        else:
            snapshot.funding_score = 0

        return snapshot

    def score(self, snapshot):
        snapshot = self.score_funding(snapshot)

        snapshot.psychology_score = snapshot.funding_score

        return snapshot
