import random
from cell import Cell


class Model:
    def __init__(self):
        self.maze_rows = 40
        self.maze_cols = 40
        self.maze = self.generate_maze()

        # Carve the maze using randomized dfs algorithm => remove walls
        self.carve_maze()

        # Determine the path from the top left corner to the bottom right one
        self.path = self.determine_path_to_end()

    @property
    def edge_length(self):
        return Cell.EDGE_LENGTH

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

    def depth_first_search(self, current_cell, visited, path):
        if current_cell in visited:
            return False, path
        if current_cell.row == self.maze_rows - 1 and current_cell.col == self.maze_cols - 1:
            return True, path

        visited.append(current_cell)

        # Get all the available cells
        adjacent_cells = self.get_adjacent_cells(current_cell)

        # Filter only the cells, to which we have access and no walls are blocking the way
        viable_adj_cells = [
            cell for cell in adjacent_cells
            if self.check_walls(current_cell, cell)
        ]

        for cell in viable_adj_cells:
            if cell not in visited:
                found_end, path = self.depth_first_search(cell, visited, path)
                if found_end:
                    path.append(cell)
                    return True, path

        return False, path

    def carve_maze(self):
        # Start carving the maze from the top left cell
        self.iterative_dfs(self.maze[0][0])

    def determine_path_to_end(self):
        found_end, path = self.depth_first_search(self.maze[0][0], [], [])

        if found_end:
            path.append(self.maze[0][0])
            path.reverse()

        return path
