import unittest
from matrix import Matrix

class TestMatrixCompleta(unittest.TestCase):

    def test_dimensoes(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(m.rows, 2)
        self.assertEqual(m.cols, 3)

    def test_soma(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        self.assertEqual((m1 + m2).data, [[6, 8], [10, 12]])

    def test_subtracao(self):
        m1 = Matrix([[5, 5], [5, 5]])
        m2 = Matrix([[1, 2], [3, 4]])
        self.assertEqual((m1 - m2).data, [[4, 3], [2, 1]])

    def test_multiplicacao(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[2, 0], [1, 2]])
        self.assertEqual((m1 * m2).data, [[4, 4], [10, 8]])

    def test_transposta(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(m.T.data, [[1, 4], [2, 5], [3, 6]])

if __name__ == '__main__':
    unittest.main()
