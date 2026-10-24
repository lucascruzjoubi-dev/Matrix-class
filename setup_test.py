# setup_test.py
import subprocess
import sys

# 1. Escreve o arquivo matrix.py corrigido com post_init garantido
matrix_code = """from dataclasses import dataclass, field

@dataclass
class Matrix:
    data: list[list[float]]
    rows: int = field(init=False)
    cols: int = field(init=False)

    def __post_init__(self):
        if not self.data or not self.data[0]:
            raise ValueError("A matriz não pode ser vazia.")
        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def __str__(self) -> str:
        return "\\n".join([str(row) for row in self.data])

    @property
    def T(self) -> 'Matrix':
        result = [[self.data[r][c] for r in range(self.rows)] for c in range(self.cols)]
        return Matrix(result)

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Dimensões incompatíveis para soma.")
        result = [[self.data[r][c] + other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(result)
"""

with open("matrix.py", "w", encoding="utf-8") as f:
    f.write(matrix_code)

# 2. Escreve o arquivo test_matrix.py correspondente
test_code = """import unittest
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
"""

with open("test_matrix.py", "w", encoding="utf-8") as f:
    f.write(test_code)

print("Arquivos matrix.py e test_matrix.py regravados com sucesso!")

# 3. Executa o teste unitário imediatamente limpando o cache
print("\\n--- Rodando os Testes Unitários Automáticos ---")
subprocess.run([sys.executable, "-m", "unittest", "test_matrix.py"])
