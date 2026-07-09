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
        snapshot = self.score_open_interest(snapshot)

        snapshot.psychology_score = (
            snapshot.funding_score
            + snapshot.oi_score
        )

        return snapshot

    def score_open_interest(self, snapshot):
        change = snapshot.oi_change_30d

        if change <= -20:
            snapshot.oi_score = 10
        elif change <= -5:
            snapshot.oi_score = 8
        elif change <= 10:
            snapshot.oi_score = 5
        else:
            snapshot.oi_score = 0

        return snapshot
