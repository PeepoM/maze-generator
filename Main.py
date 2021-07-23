from model import Model
from view import View
from controller import Controller


def main():
    model = Model()
    view = View(model.maze_rows, model.maze_cols, model.edge_length)
    controller = Controller(model, view)

    controller.game_loop()


if __name__ == '__main__':
    main()
