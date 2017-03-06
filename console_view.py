from life_model import Game


class View:
    model = None

    def __init__(self, new_model):
        self.model = new_model

    def get_game_string(self):
        game_string = [[""] * self.model.width() for _ in range(self.model.height())]
        for row in range(self.model.height()):
            for column in range(self.model.width()):
                if self.model.cell_at_point(column, row):
                    game_string[column][row] = "O"
                else:
                    game_string[column][row] = "."
        return "\n".join("".join(line) for line in game_string)

    def print_game_string(self):
        print self.get_game_string()
