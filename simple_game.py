from life_model import Game
from console_view import View
import sys


def main(file_name="input.txt"):
    with open(file_name) as input_file:
        lines = [line.rstrip('\n') for line in input_file]
    game_height = len(lines)
    game_width = len(lines[0])
    model = Game(game_width, game_height)
    for y, line in enumerate(lines):
        if len(line) != game_width:
            print "Improper input file format, input should be a rectangular grid of .O characters."
            exit(1)
        else:
            for x, char in enumerate(line):
                if char == "O":
                    model.set_live_cell(x, y)
    view = View(model)
    model.tick()
    view.print_game_string()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
