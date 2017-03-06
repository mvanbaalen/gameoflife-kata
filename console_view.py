class View:
    model = None

    def __init__(self, new_model):
        self.model = new_model

    def get_game_string(self):
        game_string = []
        for row in range(self.model.height()):
            line = []
            for column in range(self.model.width()):
                if self.model.cell_at_point(column, row):
                    line.append("O")
                else:
                    line.append(".")
            game_string.append(line)
        return "\n".join("".join(line) for line in game_string)

    def print_game_string(self):
        print self.get_game_string()
