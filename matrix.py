from dataclasses import dataclass, field

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
