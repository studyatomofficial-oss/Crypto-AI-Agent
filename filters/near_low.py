class NearLowFilter:
    @staticmethod
    def calculate_distance(current_price: float, low_price: float) -> float:
        return ((current_price - low_price) / low_price) * 100

    @staticmethod
    def is_near_low(distance: float, threshold: float = 5.0) -> bool:
        return distance <= threshold
