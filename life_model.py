class Game:

    grid = [[]]

    def __init__(self, size_x=1, size_y=1):
        # Fill an array with False (dead cell) X times to get the width
        # Do that Y times to get the height
        self.grid = [[False]*size_x for _ in range(size_y)]