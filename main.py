from model import Model
from view import View
from controller import Controller


class Main:
    def __init__(self):
        self.model = Model()
        self.view = View(self.model.maze_rows, self.model.maze_cols,
                         self.model.edge_length)
        self.controller = Controller(self.model, self.view)

    def main(self):
        self.controller.game_loop()


if __name__ == '__main__':
    Main().main()
