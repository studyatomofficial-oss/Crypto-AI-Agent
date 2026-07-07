class VolumeFilter:
    @staticmethod
    def accept(snapshot, minimum_volume: float = 1_000_000.0) -> bool:
        return snapshot.volume_24h >= minimum_volume
