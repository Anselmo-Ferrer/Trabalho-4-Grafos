import sys
from point import Point
from tour import Tour
from visualizer import showTours


def main() -> None:
    if len(sys.argv) < 2:
        raise ValueError(
            "Informe o arquivo de entrada.\n"
            "Exemplo: python main.py ../dados/tsp10.txt"
        )

    filepath = sys.argv[1]

    # Leitura do arquivo de entrada
    with open(filepath, "r") as f:
        tokens = f.read().split()

    idx = 0
    width = int(tokens[idx]);  idx += 1
    height = int(tokens[idx]); idx += 1

    points = []
    while idx + 1 < len(tokens):
        x = float(tokens[idx]); idx += 1
        y = float(tokens[idx]); idx += 1
        points.append(Point(x, y))

    print("Instancia TSP carregada:")
    print(f"- dimensoes: {width} x {height}")
    print(f"- numero de pontos: {len(points)}")

    # Construcao dos circuitos pelas duas heuristicas
    nearest = Tour()
    smallest = Tour()

    for point in points:
        nearest.insertNearest(point)
        smallest.insertSmallest(point)

    print()
    print(f"Nearest insertion:  tamanho = {nearest.size()}, comprimento = {nearest.length():.4f}")
    print(f"Smallest insertion: tamanho = {smallest.size()}, comprimento = {smallest.length():.4f}")

    # Visualizacao
    showTours(width, height, points, nearest, smallest)


if __name__ == "__main__":
    main()
