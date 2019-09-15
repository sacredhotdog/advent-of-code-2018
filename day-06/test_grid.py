import unittest
from grid import Grid


class TestGrid(unittest.TestCase):

    def test_max_size_is_calculated_correctly(self):
        grid = Grid([(8, 9)])

        # Due to zero-based indexing, the width and height should be one greater than the max indices
        self.assertEqual(grid.max_width, 9)
        self.assertEqual(grid.max_height, 10)

    def test_grid_is_populated_correctly(self):
        grid = Grid([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])

        self.assertEqual(grid.get(1, 1), "A")
        self.assertEqual(grid.get(1, 6), "B")
        self.assertEqual(grid.get(8, 3), "C")
        self.assertEqual(grid.get(3, 4), "D")
        self.assertEqual(grid.get(5, 5), "E")
        self.assertEqual(grid.get(8, 9), "F")


if __name__ == "__main__":
    unittest.main()
