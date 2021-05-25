from main import get_most_common, find_neighbours, get_neighbors_loc
from main import update_flooded, update_initial_board
import unittest
import numpy as np


class TestSum(unittest.TestCase):
    initial_board_x2 = np.array([[1, 2],
                                 [4, 5]], np.int32)
    flooded = [[0, 0]]
    most_common = 2
    neighbors = [{'position': [0, 0],
                  'value': 1,
                  'neighbors': [{'value': 2,
                                 'location': 'right',
                                 'position': [0, 1]},
                                {'value': 4,
                                 'location': 'bottom',
                                 'position': [1, 0]}]}]

    def test_most_common(self):
        self.assertEqual(get_most_common([1, 2, 2, 3]), 2, "Should be 2")

    def test_most_common_ranked(self):
        self.assertEqual(get_most_common([1, 1, 2, 2, 3, 3]), 1, "Should be 1")

    def test_find_neighbors(self):
        neighbors = TestSum.neighbors
        initial_board = TestSum.initial_board_x2
        flooded = TestSum.flooded
        self.assertEqual(find_neighbours(initial_board,
                                         flooded),
                         neighbors,
                         'Should be' + str(neighbors))

    def test_get_neighbors_loc(self):
        neighbors = TestSum.neighbors
        result = [[0, 1], [1, 0]]
        self.assertEqual(get_neighbors_loc(neighbors),
                         result,
                         "Should be "+str(result))

    def test_update_flooded(self):
        most_common = TestSum.most_common
        neighbors = TestSum.neighbors
        flooded = TestSum.flooded
        result = [[0, 0], [0, 1]]
        self.assertEqual(update_flooded(flooded,
                                        neighbors,
                                        most_common),
                         result,
                         "Should be "+str(result))

    def test_update_initial_board(self):
        most_common = TestSum.most_common
        initial_board = TestSum.initial_board_x2
        flooded = TestSum.flooded
        result = np.array([[2, 2], [4, 5]], np.int32)
        self.assertEquals(update_initial_board(initial_board,
                                               flooded,
                                               most_common),
                          result,
                          "Should be "+str(result))


if __name__ == '__main__':
    unittest.main()
