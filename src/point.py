import math


class Point:
    """Ponto 2D imutavel com coordenadas de ponto flutuante."""

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def distanceTo(self, other: "Point") -> float:
        """Retorna a distancia euclidiana entre este ponto e outro."""
        dx = self._x - other._x
        dy = self._y - other._y
        return math.sqrt(dx * dx + dy * dy)

    def __repr__(self) -> str:
        return f"({self._x}, {self._y})"
