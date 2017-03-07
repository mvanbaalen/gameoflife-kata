from console_view import View
from life_model import Game
import unittest


class TestRequirements(unittest.TestCase):
    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    def test_that_new_view_is_blank(self):
        blank_game = Game(5, 5)
        blank_view = View(blank_game)
        comparison_string = """\
.....
.....
.....
.....
....."""
        self.assertEqual(blank_view.get_game_string(), comparison_string)

    def test_that_view_with_1_live_cell_displays(self):
        game = Game(5, 5)
        game.set_live_cell(1, 2)
        view = View(game)
        comparison_string = """\
.....
.....
.O...
.....
....."""
        self.assertEqual(view.get_game_string(), comparison_string)

    def test_that_view_with_many_live_cells_displays(self):
        game = Game(5, 5)
        game.set_live_cell(0, 0)
        game.set_live_cell(1, 1)
        game.set_live_cell(2, 1)
        game.set_live_cell(2, 3)
        view = View(game)
        comparison_string = """\
O....
.OO..
.....
..O..
....."""
        self.assertEqual(view.get_game_string(), comparison_string)

    def test_that_single_row_game_displays_on_one_line(self):
        game = Game(10, 1)
        view = View(game)
        comparison_string = ".........."
        self.assertEqual(view.get_game_string(), comparison_string)

    def test_that_single_column_game_display_one_per_line(self):
        game = Game(1, 10)
        view = View(game)
        comparison_string = """\
.
.
.
.
.
.
.
.
.
."""
        self.assertEqual(view.get_game_string(), comparison_string)

    def test_that_model_can_change_after_view(self):
        game = Game(2, 2)
        view = View(game)
        game.set_live_cell(0, 0)
        comparison_string = """\
O.
.."""
        self.assertEqual(view.get_game_string(), comparison_string)
