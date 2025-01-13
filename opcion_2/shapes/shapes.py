class Shape:
    def __init__(self, is_regular: bool = False):
        self.is_regular = is_regular
        self.vertices = []
        self.edges = []
        self.inner_angles = [] 

    def compute_area(self):
        ...

    def compute_perimeter(self):
        ...