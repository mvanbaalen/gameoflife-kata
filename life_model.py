class Game:
    grid = [[]]

    def __init__(self, size_x=1, size_y=1):
        # Fill an array with False (dead cell) X times to get the width
        # Do that Y times to get the height
        self.grid = [[False] * size_x for _ in range(size_y)]

    def width(self):
        return len(self.grid[0])

    def height(self):
        return len(self.grid)

    def cell_at_point(self, x, y):
        """
        Check if a living cell is at point x, y
        :param x:
        :param y:
        :return: true if there is a living cell, or false if there is not
        Throws an IndexError if that point is outside of the bounds of the game
        """
        return self.grid[y][x]

    def set_live_cell(self, x, y):
        """
        Set cell to live at point x, y
        :param x:
        :param y:
        Throws IndexError if that point is outside of the bounds of the game
        """
        self.grid[y][x] = True

    def set_dead_cell(self, x, y):
        """
        Set cell to dead at point x, y
        :param x:
        :param y:
        Throws IndexError if that point is outside of the bounds of the game
        """
        self.grid[y][x] = False

    def check_neighbors_at_point(self, x, y):
        """
        Find the number of neighbors for a given point on the grid
        :param x:
        :param y:
        :return: an integer from 0 to 8 based on the living cells next to this point
        Throws IndexError if that point is outside of the bounds of the game
        """
        neighbors = 0
        for check_x in [x - 1, x, x + 1]:
            for check_y in [y - 1, y, y + 1]:
                try:
                    if self.cell_at_point(check_x, check_y) and check_x >= 0 and check_y >= 0:
                        neighbors += 1
                # We can treat out of bounds like a dead neighbor
                except IndexError:
                    pass
        # Can't be your own neighbor, but it will be counted previously
        if self.cell_at_point(x, y):
            neighbors -= 1
        return neighbors

    def cell_at_next_tick(self, x, y):
        """
        Check if a cell will be live during the next game tick
        :param x:
        :param y:
        :return:
        """
        neighbors = self.check_neighbors_at_point(x, y)
        if self.cell_at_point(x, y):
            if neighbors < 2 or neighbors > 3:
                return False
            else:
                return True
        else:
            if neighbors == 3:
                return True
            else:
                return False

    def tick(self):
        """
        Perform all Game of Life rules and update the model permanently
        """
        buffer_grid = [[False] * len(self.grid[0]) for _ in self.grid]
        for row_num in range(len(self.grid)):
            for col_num in range(len(self.grid[0])):
                buffer_grid[row_num][col_num] = self.cell_at_next_tick(row_num, col_num)
        self.grid = buffer_grid
