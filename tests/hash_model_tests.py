import unittest

import hash_model


class HashModelTest(unittest.TestCase):
    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    # Exposed method tests
    # These tests verify that the methods that will be called by the View or Controller are performing correctly
    # These should be uncoupled from the specific implementation, if that changes

    def test_that_new_game_has_dead_cell(self):
        new_game = hash_model.Game()
        self.assertEqual(new_game.cell_at_point(0, 0), False)

    # NOTE: In an infinite game, this should return false instead!
    def test_that_new_game_cell_out_of_bounds(self):
        new_game = hash_model.Game()
        self.assertRaises(IndexError, new_game.cell_at_point, 1, 1)

    def test_that_a_live_cell_can_be_created(self):
        game = hash_model.Game()
        game.set_live_cell(0, 0)
        self.assertEqual(game.cell_at_point(0, 0), True)

    # NOTE: In an infinite game, this should not throw an Exception
    def test_that_created_cell_out_of_bounds(self):
        game = hash_model.Game()
        self.assertRaises(IndexError, game.set_live_cell, 1, 1)

    def test_that_live_cell_set_live_still_lives(self):
        game = hash_model.Game()
        game.set_live_cell(0, 0)
        game.set_live_cell(0, 0)
        self.assertEqual(game.cell_at_point(0, 0), True)

    def test_that_a_live_cell_can_be_set_dead(self):
        game = hash_model.Game()
        game.set_live_cell(0, 0)
        game.set_dead_cell(0, 0)
        self.assertEqual(game.cell_at_point(0, 0), False)

    # NOTE: In an infinite game, this should not throw an Exception
    def test_that_set_dead_cell_out_of_bounds(self):
        game = hash_model.Game()
        self.assertRaises(IndexError, game.set_dead_cell, 1, 1)

    def test_that_dead_cell_set_dead_still_dead(self):
        game = hash_model.Game()
        game.set_dead_cell(0, 0)
        self.assertEqual(game.cell_at_point(0, 0), False)

    def test_that_empty_grid_cell_will_be_dead(self):
        game = hash_model.Game()
        self.assertEqual(game.cell_at_next_tick(0, 0), False)

    def test_that_dead_cell_with_3_neighbors_will_live(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(1, 0)
        game.set_live_cell(1, 1)
        game.set_live_cell(1, 2)
        self.assertEqual(game.cell_at_next_tick(0, 1), True)
        self.assertEqual(game.cell_at_next_tick(2, 1), True)

    def test_that_dead_cell_with_2_neighbors_remains_dead(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(1, 0)
        game.set_live_cell(1, 1)
        game.set_live_cell(1, 2)
        self.assertEqual(game.cell_at_next_tick(0, 0), False)
        self.assertEqual(game.cell_at_next_tick(2, 0), False)
        self.assertEqual(game.cell_at_next_tick(0, 0), False)
        self.assertEqual(game.cell_at_next_tick(2, 0), False)

    def test_that_dead_cell_with_4_neighbors_remains_dead(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(0, 0)
        game.set_live_cell(1, 0)
        game.set_live_cell(2, 0)
        game.set_live_cell(0, 1)
        self.assertEqual(game.cell_at_next_tick(1, 1), False)

    def test_that_live_cell_with_4_neighbors_will_die(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(0, 0)
        game.set_live_cell(0, 1)
        game.set_live_cell(1, 1)
        game.set_live_cell(1, 0)
        game.set_live_cell(2, 0)
        self.assertEqual(game.cell_at_next_tick(1, 1), False)

    def test_that_live_cell_with_1_neighbor_will_die(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(0, 0)
        game.set_live_cell(0, 1)
        self.assertEqual(game.cell_at_next_tick(0, 0), False)
        self.assertEqual(game.cell_at_next_tick(0, 1), False)

    def test_that_live_cell_with_2_neighbors_will_live(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(0, 0)
        game.set_live_cell(0, 1)
        game.set_live_cell(1, 0)
        self.assertEqual(game.cell_at_next_tick(0, 0), True)
        self.assertEqual(game.cell_at_next_tick(0, 1), True)
        self.assertEqual(game.cell_at_next_tick(1, 0), True)

    def test_that_empty_grid_has_0_neighbors(self):
        game = hash_model.Game(3, 3)
        self.assertEqual(game.check_neighbors_at_point(1, 1), 0)

    def test_that_single_cell_has_0_neighbors(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(1, 1)
        self.assertEqual(game.check_neighbors_at_point(1, 1), 0)

    def test_that_empty_edge_cell_has_0_neighbors(self):
        game = hash_model.Game(3, 3)
        self.assertEqual(game.check_neighbors_at_point(0, 1), 0)

    def test_that_two_cells_are_each_neighbors(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(1, 1)
        game.set_live_cell(1, 2)
        self.assertEqual(game.check_neighbors_at_point(1, 1), 1)
        self.assertEqual(game.check_neighbors_at_point(1, 2), 1)

    def test_that_full_grid_has_correct_neighbors(self):
        game = hash_model.Game(3, 3)
        for x in range(3):
            for y in range(3):
                game.set_live_cell(x, y)
        self.assertEqual(game.check_neighbors_at_point(0, 0), 3)
        self.assertEqual(game.check_neighbors_at_point(0, 1), 5)
        self.assertEqual(game.check_neighbors_at_point(1, 1), 8)

    def test_that_tick_runs(self):
        game = hash_model.Game(3, 3)
        game.tick()
        self.assertEqual(game.cell_at_point(0, 0), False)

    def test_that_cells_are_created_by_tick(self):
        game = hash_model.Game(4, 4)
        game.set_live_cell(1, 1)
        game.set_live_cell(2, 1)
        game.set_live_cell(3, 1)
        game.tick()
        self.assertEqual(game.cell_at_point(2, 2), True)

    def test_that_cells_are_destroyed_by_tick(self):
        game = hash_model.Game(2, 2)
        game.set_live_cell(0, 0)
        game.set_live_cell(1, 1)
        game.tick()
        self.assertEqual(game.cell_at_point(0, 0), False)
        self.assertEqual(game.cell_at_point(1, 1), False)

    def test_that_two_ticks_complete(self):
        game = hash_model.Game(3, 3)
        game.set_live_cell(1, 0)
        game.set_live_cell(1, 1)
        game.set_live_cell(1, 2)
        game.tick()
        game.tick()
        self.assertEqual(game.cell_at_point(1, 0), True)
        self.assertEqual(game.cell_at_point(1, 1), True)
        self.assertEqual(game.cell_at_point(1, 2), True)

    def test_that_new_game_size_is_accurate(self):
        game = hash_model.Game(8, 2)
        self.assertEqual(game.width(), 8)
        self.assertEqual(game.height(), 2)

    def test_that_edge_cells_tick_correctly(self):
        game = hash_model.Game(2, 2)
        game.set_live_cell(0, 0)
        game.set_live_cell(0, 1)
        game.set_live_cell(1, 0)
        game.set_live_cell(1, 1)
        game.tick()
        self.assertEqual(game.cell_at_point(0, 0), True)
        self.assertEqual(game.cell_at_point(1, 0), True)
        self.assertEqual(game.cell_at_point(1, 1), True)
        self.assertEqual(game.cell_at_point(1, 1), True)

    def test_that_uneven_grid_ticks_correctly(self):
        game = hash_model.Game(8, 6)
        game.tick()
