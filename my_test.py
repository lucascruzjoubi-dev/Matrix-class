from dataclasses import dataclass

@dataclass
class Matrix:
    data: list[list[float]]

    @property
    def rows(self) -> int:
        """Calcula dinamicamente a quantidade de linhas."""
        return len(self.data)

    @property
    def cols(self) -> int:
        """Calcula dinamicamente a quantidade de colunas."""
        if not self.data or not self.data:
            return 0
        return len(self.data[0])

    def __str__(self) -> str:
        return "\n".join([str(row) for row in self.data])

    @property
    def T(self) -> 'Matrix':
        result = [[self.data[r][c] for r in range(self.rows)] for c in range(self.cols)]
        return Matrix(result)

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Dimensões incompatíveis para soma.")
        result = [[self.data[r][c] + other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Dimensões incompatíveis para subtração.")
        result = [[self.data[r][c] - other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError("Dimensões incompatíveis para multiplicação.")
        result = [[sum(self.data[r][k] * other.data[k][c] for k in range(self.cols)) for c in range(other.cols)] for r in range(self.rows)]
        return Matrix(result)

# ==========================================
# CÓDIGO DE TESTE (Roda automaticamente na IDE)
# ==========================================
if __name__ == "__main__":
    print("--- Inicializando Matriz A ---")
    A = Matrix([[1, 1, 1], [1, 1, 1]])
    print(f"Matriz A:\n{A}")
    print(f"Linhas de A: {A.rows}")
    print(f"Colunas de A: {A.cols}")
    
    print("\n--- Testando a Transposta (.T) ---")
    print(f"Matriz A Transposta:\n{A.T}")

    print("\n--- Testando Operações ---")
    B = Matrix([[1, 1, 1], [1, 1, 1]])
    print(f"Matriz B:\n{B}")
    print(f"Soma (A + B):\n{A + B}")
