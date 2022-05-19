import random
from cell import Cell
from collections import deque


class Model:
    def __init__(self):
        self.maze_rows = 40
        self.maze_cols = 40
        self.maze = self.generate_maze()

        # Carve the maze using randomized dfs algorithm => remove walls
        self.carve_maze()

        # Determine the path from the top left corner to the bottom right one
        self._path = self.determine_path_to_end()

    @property
    def edge_length(self):
        return Cell.EDGE_LENGTH

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def generate_maze(self):
        return [[Cell(row, col) for col in range(self.maze_cols)]
                for row in range(self.maze_rows)]

    def get_adjacent_cells(self, current_cell):
        row = current_cell.row
        col = current_cell.col

        adj_cells = []

        if row < self.maze_rows - 1:
            adj_cells.append(self.maze[row + 1][col])
        if row > 0:
            adj_cells.append(self.maze[row - 1][col])
        if col < self.maze_cols - 1:
            adj_cells.append(self.maze[row][col + 1])
        if col > 0:
            adj_cells.append(self.maze[row][col - 1])

        return adj_cells

    def remove_walls(self, current_cell, adjacent_cell):
        cur_row = current_cell.row
        cur_col = current_cell.col
        adj_row = adjacent_cell.row
        adj_col = adjacent_cell.col

        if cur_row < adj_row:
            current_cell.walls["bottom"] = False
        if cur_row > adj_row:
            adjacent_cell.walls["bottom"] = False
        if cur_col < adj_col:
            current_cell.walls["right"] = False
        if cur_col > adj_col:
            adjacent_cell.walls["right"] = False

    def iterative_dfs(self, starting_cell):
        visited = []
        stack = []

        visited.append(starting_cell)
        stack.append(starting_cell)

        while stack:
            current_cell = stack.pop()

            # Get all the adjacent cell to the current cell
            adjacent_cells = self.get_adjacent_cells(current_cell)

            # Filter out those adjacent cells, that are unvisited
            unvisited_adj_cells = [
                cell for cell in adjacent_cells if cell not in visited
            ]

            if unvisited_adj_cells:
                stack.append(current_cell)

                # Choose a random cell out of all the unvisited adjacent cells
                cell = random.choice(unvisited_adj_cells)

                # Remove walls between the current cell and the random unvisited adjacent cell
                self.remove_walls(current_cell, cell)

                visited.append(cell)
                stack.append(cell)

    def check_walls(self, current_cell, adjacent_cell):
        row = current_cell.row
        col = current_cell.col

        if adjacent_cell.row > row and not current_cell.walls["bottom"]:
            return True
        elif adjacent_cell.row < row and not adjacent_cell.walls["bottom"]:
            return True
        elif adjacent_cell.col > col and not current_cell.walls["right"]:
            return True
        elif adjacent_cell.col < col and not adjacent_cell.walls["right"]:
            return True

        return False

    def depth_first_search(self, start_cell, end_cell):
        visited = set()
        stack = deque([start_cell])

        while stack:
            cell = stack.pop()

            if cell == end_cell:
                return True

            if cell not in visited:
                visited.add(cell)

                viable_adj_cells = [adj_cell for adj_cell in self.get_adjacent_cells(cell)
                                    if self.check_walls(cell, adj_cell)]

                for adj_cell in viable_adj_cells:
                    if adj_cell not in visited:
                        adj_cell.parent = cell
                        stack.append(adj_cell)

        return False

    def carve_maze(self):
        # Start carving the maze from the top left cell
        self.iterative_dfs(self.maze[0][0])

    def determine_path_to_end(self):
        start_cell = self.maze[0][0]
        end_cell = self.maze[-1][-1]
        found_end = self.depth_first_search(start_cell, end_cell)

        if found_end:
            return end_cell.reconstruct_path()
