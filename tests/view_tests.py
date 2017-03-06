from console_view import View
from life_model import Game
import unittest


class TestRequirements(unittest.TestCase):
    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    def test_that_new_view_is_blank(self):
        blank_game = Game(5, 5)
        blank_view = View(blank_game)
        comparison_string = \
            """\
.....
.....
.....
.....
....."""
        self.assertEqual(blank_view.get_game_string(), comparison_string)

    def test_that_view_with_1_live_cell_displays(self):
        game = Game(5, 5)
        game.set_live_cell(1,2)
        view = View(game)
        view.print_game_string()
        comparison_string = \
            """\
.....
.....
.O...
.....
....."""
        self.assertEqual(view.get_game_string(), comparison_string)
