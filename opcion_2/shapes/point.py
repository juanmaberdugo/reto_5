class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def compute_distance(self, point: "Point") -> float:
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
