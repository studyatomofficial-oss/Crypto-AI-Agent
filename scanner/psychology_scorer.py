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
        snapshot = self.score_crowd(snapshot)
        snapshot = self.score_base(snapshot)
        snapshot = self.score_false_break(snapshot)
        snapshot = self.score_recovery_failure(snapshot)

        snapshot.psychology_score = (
            snapshot.funding_score
            + snapshot.oi_score
            + snapshot.crowd_score
            + snapshot.base_score
            + snapshot.false_break_score
            + snapshot.recovery_failure_score
        )

        return snapshot

    def score_open_interest(self, snapshot):
        changes = []
        if snapshot.oi_avg_7d > 0:
            changes.append(snapshot.oi_vs_7d_avg)
        if snapshot.oi_avg_30d > 0:
            changes.append(snapshot.oi_vs_30d_avg)

        if not changes:
            snapshot.oi_score = 0
            return snapshot

        change = sum(changes) / len(changes)

        if change <= -25:
            snapshot.oi_score = 10
        elif change <= -15:
            snapshot.oi_score = 7
        elif change <= -8:
            snapshot.oi_score = 5
        elif change <= -3:
            snapshot.oi_score = 3
        else:
            snapshot.oi_score = 0

        return snapshot

    def score_crowd(self, snapshot):
        dryup = snapshot.volume_dryup

        if dryup >= 70:
            snapshot.crowd_score = 10
        elif dryup >= 50:
            snapshot.crowd_score = 8
        elif dryup >= 30:
            snapshot.crowd_score = 5
        elif dryup >= 10:
            snapshot.crowd_score = 2
        else:
            snapshot.crowd_score = 0

        return snapshot

    def score_base(self, snapshot):
        adr = snapshot.avg_daily_range

        if adr <= 3:
            snapshot.base_score = 10
        elif adr <= 5:
            snapshot.base_score = 8
        elif adr <= 8:
            snapshot.base_score = 5
        elif adr <= 12:
            snapshot.base_score = 2
        else:
            snapshot.base_score = 0

        return snapshot

    def score_false_break(self, snapshot):
        snapshot.false_break_detected = False
        snapshot.false_break_score = 0

        candles = snapshot.candles
        if len(candles) < 16:
            return snapshot

        lookback = candles[-15:]
        prior = candles[:-15]
        previous_30d_low = min(candle.low for candle in prior)

        for index, candle in enumerate(lookback):
            if candle.low >= previous_30d_low:
                continue

            snapshot.false_break_detected = True

            reclaim_delay = None
            reclaim_close = None
            for j in range(index, len(lookback)):
                if lookback[j].close > previous_30d_low:
                    reclaim_delay = j - index
                    reclaim_close = lookback[j].close
                    break

            if reclaim_delay is None:
                snapshot.false_break_score = 0
            else:
                break_depth = ((previous_30d_low - candle.low) / previous_30d_low) * 100
                reclaim_strength = max(
                    0.0,
                    ((reclaim_close - previous_30d_low) / previous_30d_low) * 100,
                )

                if reclaim_delay <= 1 and reclaim_strength >= 1.0 and break_depth <= 3.0:
                    snapshot.false_break_score = 10
                elif reclaim_delay <= 3 and reclaim_strength >= 0.5 and break_depth <= 5.0:
                    snapshot.false_break_score = 7
                elif reclaim_delay <= 5 and break_depth <= 8.0:
                    snapshot.false_break_score = 5
                else:
                    snapshot.false_break_score = 3
            break

        return snapshot

    def score_recovery_failure(self, snapshot):
        recovery = snapshot.recovery_percent

        if recovery <= 5:
            snapshot.recovery_failure_score = 10
        elif recovery <= 10:
            snapshot.recovery_failure_score = 8
        elif recovery <= 20:
            snapshot.recovery_failure_score = 5
        elif recovery <= 30:
            snapshot.recovery_failure_score = 2
        else:
            snapshot.recovery_failure_score = 0

        return snapshot

