class Cell:
    EDGE_LENGTH = 20

    def __init__(self, row, col):
        self.edge_length = Cell.EDGE_LENGTH
        self.row = row
        self.col = col
        self.walls = {"bottom": True, "right": True}
        self.parent = None

    def reconstruct_path(self):
        path = []
        current = self

        while current:
            path.append(current)
            current = current.parent

        path.reverse()
        return path

    @property
    def x(self):
        return self.col * self.edge_length

    @property
    def y(self):
        return self.row * self.edge_length
