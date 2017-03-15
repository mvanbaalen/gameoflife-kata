class Game:
    size_x = 0
    size_y = 0
    can_grow = False
    grid = None

    def __init__(self, size_x=1, size_y=1, grows=False):
        # Fill an array with False (dead cell) X times to get the width
        # Do that Y times to get the height
        self.size_x = size_x
        self.size_y = size_y
        self.can_grow = grows
        self.grid = set()

    def width(self):
        return self.size_x

    def height(self):
        return self.size_y

    def check_bounds(self, x, y):
        if (not self.can_grow) and (x >= self.size_x or y >= self.size_y):
            raise IndexError

    def cell_at_point(self, x, y):
        """
        Check if a living cell is at point x, y
        :param x:
        :param y:
        :return: true if there is a living cell, or false if there is not
        Throws an IndexError if that point is outside of the bounds of the game
        """
        self.check_bounds(x, y)
        return (x, y) in self.grid

    def set_live_cell(self, x, y):
        """
        Set cell to live at point x, y
        :param x:
        :param y:
        Throws IndexError if that point is outside of the bounds of the game
        """
        self.check_bounds(x, y)
        self.grid.add((x, y))

    def set_dead_cell(self, x, y):
        """
        Set cell to dead at point x, y
        :param x:
        :param y:
        Throws IndexError if that point is outside of the bounds of the game
        """
        self.check_bounds(x, y)
        self.grid.discard((x, y))

    def check_neighbors_at_point(self, x, y):
        """
        Find the number of neighbors for a given point on the grid
        :param x:
        :param y:
        :return: an integer from 0 to 8 based on the living cells next to this point
        Throws IndexError if that point is outside of the bounds of the game
        """
        self.check_bounds(x, y)
        neighbors = 0
        for check_x in [x - 1, x, x + 1]:
            for check_y in [y - 1, y, y + 1]:
                try:
                    if self.cell_at_point(check_x, check_y):
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
        # We want to look at every live cell and its neighbors (once)
        coordinates_to_check = set()
        for cell_x, cell_y in self.grid:
            for x in [cell_x - 1, cell_x, cell_x + 1]:
                for y in [cell_y - 1, cell_y, cell_y + 1]:
                    try:
                        self.check_bounds(x, y)
                        coordinates_to_check.add((x, y))
                    except IndexError:
                        pass

        buffer_grid = set()
        for check_x, check_y in coordinates_to_check:
            if self.cell_at_next_tick(check_x, check_y):
                buffer_grid.add((check_x, check_y))
        self.grid = buffer_grid
