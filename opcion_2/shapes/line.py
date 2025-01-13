from .point import Point

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point

    def compute_length(self) -> float:
        return self.start_point.compute_distance(self.end_point)