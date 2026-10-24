from dataclasses import dataclass, field

@dataclass
class Matrix:
    data: list[list[float]]
    rows: int = field(init=False)
    cols: int = field(init=False)

    def __post_init__(self):
        """Garante a criação imediata e correta de rows e cols."""
        if not self.data or not self.data[0]:
            raise ValueError("A matriz não pode ser vazia.")
        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def __str__(self) -> str:
        """Formata o print para exibir as linhas empilhadas."""
        return "\n".join([str(row) for row in self.data])

    @property
    def T(self) -> 'Matrix':
        """Retorna a matriz transposta."""
        result = [[self.data[r][c] for r in range(self.rows)] for c in range(self.cols)]
        return Matrix(result)

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Soma matricial (+)."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Dimensões incompatíveis para soma.")
        result = [[self.data[r][c] + other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Subtração matricial (-)."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Dimensões incompatíveis para subtração.")
        result = [[self.data[r][c] - other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        """Multiplicação matricial (*)."""
        if self.cols != other.rows:
            raise ValueError("Dimensões incompatíveis para multiplicação.")
        result = [[sum(self.data[r][k] * other.data[k][c] for k in range(self.cols)) for c in range(other.cols)] for r in range(self.rows)]
        return Matrix(result)
