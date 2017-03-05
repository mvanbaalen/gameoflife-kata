class Game:
    grid = [[]]

    def __init__(self, size_x=1, size_y=1):
        # Fill an array with False (dead cell) X times to get the width
        # Do that Y times to get the height
        self.grid = [[False] * size_x for _ in range(size_y)]

    def cell_at_point(self, x, y):
        """
        Check if a living cell is at point x, y
        :param x:
        :param y:
        :return: true if there is a living cell, or false if there is not
        Throws an IndexError if that point is outside of the bounds of the game
        """
        return self.grid[x][y]

    def set_live_cell(self, x, y):
        """
        Set cell to live at point x, y
        :param x:
        :param y:
        Throws IndexError if that point is outside of the bounds of the game
        """
        self.grid[x][y] = True

    def set_dead_cell(self, x, y):
        """
        Set cell to dead at point x, y
        :param x:
        :param y:
        Throws IndexError if that point is outside of the bounds of the game
        """
        self.grid[x][y] = False
