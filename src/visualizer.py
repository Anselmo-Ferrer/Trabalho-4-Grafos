from __future__ import annotations
from typing import List

try:
    import matplotlib.pyplot as plt
    import matplotlib.lines as mlines
    _HAS_MATPLOTLIB = True
except ImportError:
    _HAS_MATPLOTLIB = False

from point import Point
from tour import Tour


def showTours(width: int, height: int, points: List[Point],
              nearest: Tour, smallest: Tour) -> None:
    """
    Exibe os dois circuitos (tours) lado a lado em subplots separados.

    - Esquerda: Nearest insertion (VERMELHO)
    - Direita:  Smallest insertion (AZUL)
    - Os pontos da instancia aparecem em PRETO em ambos.
    """
    if not _HAS_MATPLOTLIB:
        _print_text_fallback(points, nearest, smallest)
        return

    n = len(points)
    dot_size = 6 if n <= 100 else (2 if n <= 1000 else 0.5)
    dot_alpha = 1.0 if n <= 100 else (0.6 if n <= 1000 else 0.3)

    px = [p.x for p in points]
    py = [p.y for p in points]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle(f"TSP Heuristicas de Insercao  —  {n} pontos", fontsize=13)

    for ax, tour, color, label in (
        (ax1, nearest,  "red",  f"Nearest insertion\ncomprimento: {nearest.length():.4f}"),
        (ax2, smallest, "blue", f"Smallest insertion\ncomprimento: {smallest.length():.4f}"),
    ):
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.set_title(label, fontsize=11, color=color)
        ax.set_xticks([])
        ax.set_yticks([])

        t_pts = tour.points()
        if t_pts:
            xs = [p.x for p in t_pts] + [t_pts[0].x]
            ys = [p.y for p in t_pts] + [t_pts[0].y]
            ax.plot(xs, ys, color=color, linewidth=0.8, zorder=1)

        ax.scatter(px, py, color="black", s=dot_size, alpha=dot_alpha, zorder=2)

    plt.tight_layout()
    plt.show()


def _print_text_fallback(points, nearest, smallest):
    """Fallback textual caso matplotlib nao esteja disponivel."""
    print("\n[visualizacao indisponivel — instale matplotlib: pip install matplotlib]")
    print(f"num points : {len(points)}")
    print(f"nearest    : {nearest.length():.4f}")
    print(f"smallest   : {smallest.length():.4f}")
