import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_dimensions(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(m.rows, 2)
        self.assertEqual(m.cols, 3)

    def test_addition(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1 + m2
        self.assertEqual(result.data, [[6, 8], [10, 12]])
