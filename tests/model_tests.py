import unittest
import life_model


class TestRequirements(unittest.TestCase):
    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    # Implementation Unit Tests
    # These tests test the specific implementation of the grid, if the implementation changes, then these tests must
    # change as well. Or, if these tests change, the implementation must also change.

    def test_that_new_grid_has_one_cell(self):
        one_game = life_model.Game()
        self.assertEqual(one_game.grid, [[False]])

    def test_that_new_grid_of_size_3_has_3(self):
        three_game = life_model.Game(3, 3)
        self.assertEqual(three_game.grid, [[False, False, False],
                                           [False, False, False],
                                           [False, False, False]])

    def test_that_new_uneven_grid_2_3_has_2_3(self):
        uneven_game = life_model.Game(2, 3)
        self.assertEqual(uneven_game.grid, [[False, False],
                                            [False, False],
                                            [False, False]])

    # Exposed method tests
    # These tests verify that the methods that will be called by the View or Controller are performing correctly
    # These should be uncoupled from the specific implementation, if that changes

    def test_that_new_game_has_dead_cell(self):
        new_game = life_model.Game()
        self.assertEqual(new_game.cell_at_point(0, 0), False)

    # NOTE: In an infinite game, this should return false instead!
    def test_that_new_game_cell_out_of_bounds(self):
        new_game = life_model.Game()
        self.assertRaises(IndexError, new_game.cell_at_point, 1, 1)

    def test_that_a_live_cell_can_be_created(self):
        game = life_model.Game()
        game.set_live_cell(0, 0)
        self.assertEqual(game.cell_at_point(0, 0), True)

    # NOTE: In an infinite game, this should not throw an Exception
    def test_that_created_cell_out_of_bounds(self):
        game = life_model.Game()
        self.assertRaises(IndexError, game.set_live_cell, 1, 1)

    def test_that_live_cell_set_live_still_lives(self):
        game = life_model.Game()
        game.set_live_cell(0, 0)
        game.set_live_cell(0, 0)
        self.assertEqual(game.cell_at_point(0, 0), True)

    def test_that_a_live_cell_can_be_set_dead(self):
        game = life_model.Game()
        game.set_live_cell(0, 0)
        game.set_dead_cell(0, 0)
        self.assertEqual(game.cell_at_point(0, 0), False)

    # NOTE: In an infinite game, this should not throw an Exception
    def test_that_set_dead_cell_out_of_bounds(self):
        game = life_model.Game()
        self.assertRaises(IndexError, game.set_dead_cell, 1, 1)

    def test_that_dead_cell_set_dead_still_dead(self):
        game = life_model.Game()
        game.set_dead_cell(0, 0)
        self.assertEqual(game.cell_at_point(0, 0), False)
