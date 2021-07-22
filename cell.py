class Cell:
    EDGE_LENGTH = 20
    
    def __init__(self, row, col):
        self.edge_length = Cell.EDGE_LENGTH
        self.row = row
        self.col = col
        self.walls = {"bottom": True, "right": True}
    
    @property
    def x(self):
        return self.col * self.edge_length
    
    @property
    def y(self):
        return self.row * self.edge_length
