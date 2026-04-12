from __future__ import annotations
from point import Point


class Tour:
    """
    Circuito (tour) representado como lista encadeada circular.

    Cada no armazena um Point e um ponteiro para o proximo no.
    Os metodos insertNearest e insertSmallest implementam as duas
    heuristicas de insercao para o TSP.
    """

    class _Node:
        __slots__ = ("p", "next")

        def __init__(self, p: Point = None):
            self.p: Point = p
            self.next: "Tour._Node" = None

    def __init__(self):
        self._start: Tour._Node = None

    def size(self) -> int:
        """Retorna o numero de pontos no circuito."""
        if self._start is None:
            return 0
        count = 0
        current = self._start
        while True:
            count += 1
            current = current.next
            if current is self._start:
                break
        return count

    def length(self) -> float:
        """Retorna o comprimento total do circuito."""
        if self._start is None:
            return 0.0
        total = 0.0
        current = self._start
        while True:
            total += current.p.distanceTo(current.next.p)
            current = current.next
            if current is self._start:
                break
        return total

    def __str__(self) -> str:
        if self._start is None:
            return ""
        parts = []
        current = self._start
        while True:
            parts.append(str(current.p))
            current = current.next
            if current is self._start:
                break
        return "\n".join(parts)

    def points(self) -> list:
        """Retorna a lista de pontos na ordem do circuito (para visualizacao)."""
        if self._start is None:
            return []
        result = []
        current = self._start
        while True:
            result.append(current.p)
            current = current.next
            if current is self._start:
                break
        return result

    # ------------------------------------------------------------------
    # Heuristica 1: nearest insertion
    # ------------------------------------------------------------------

    def insertNearest(self, p: Point) -> None:
        """
        Insere o ponto p no circuito usando a heuristica nearest insertion.

        Algoritmo:
          1. Se o circuito estiver vazio ou tiver apenas um no, insere p
             diretamente (sem escolha de posicao).
          2. Caso contrario, percorre todos os nos do circuito e identifica
             aquele cuja distancia a p e minima (no mais proximo de p).
          3. Insere p imediatamente apos esse no mais proximo.

        A heuristica prioriza a PROXIMIDADE: o proximo no a ser inserido e
        aquele mais proximo de alguma cidade ja presente no circuito.
        """
        node = Tour._Node(p)

        # Circuito vazio: cria tour de um so ponto (aponta para si mesmo)
        if self._start is None:
            node.next = node
            self._start = node
            return

        # Circuito com um unico no: insere apos ele
        if self._start.next is self._start:
            node.next = self._start
            self._start.next = node
            return

        # Encontra o no mais proximo de p
        nearest_node = self._start
        min_dist = p.distanceTo(self._start.p)

        current = self._start.next
        while current is not self._start:
            d = p.distanceTo(current.p)
            if d < min_dist:
                min_dist = d
                nearest_node = current
            current = current.next

        # Insere p logo apos o no mais proximo
        node.next = nearest_node.next
        nearest_node.next = node

    # ------------------------------------------------------------------
    # Heuristica 2: smallest insertion
    # ------------------------------------------------------------------

    def insertSmallest(self, p: Point) -> None:
        """
        Insere o ponto p no circuito usando a heuristica smallest insertion.

        Algoritmo:
          1. Se o circuito estiver vazio ou tiver apenas um no, insere p
             diretamente (sem escolha de posicao).
          2. Caso contrario, testa todas as posicoes possiveis de insercao:
             para cada aresta (A -> B) do circuito atual, calcula o aumento
             no comprimento total caso p seja inserido entre A e B:
               aumento = dist(A, p) + dist(p, B) - dist(A, B)
          3. Insere p na posicao que produz o MENOR aumento no comprimento
             do circuito.

        A heuristica prioriza o MENOR CUSTO DE INSERCAO, independentemente
        de qual cidade e escolhida ou de sua proximidade ao circuito.
        """
        node = Tour._Node(p)

        # Circuito vazio: cria tour de um so ponto
        if self._start is None:
            node.next = node
            self._start = node
            return

        # Circuito com um unico no: insere apos ele
        if self._start.next is self._start:
            node.next = self._start
            self._start.next = node
            return

        # Avalia todas as posicoes e escolhe a de menor aumento
        best_node = self._start
        min_increase = float("inf")

        current = self._start
        while True:
            # Custo de inserir p entre current e current.next
            increase = (
                current.p.distanceTo(p)
                + p.distanceTo(current.next.p)
                - current.p.distanceTo(current.next.p)
            )
            if increase < min_increase:
                min_increase = increase
                best_node = current
            current = current.next
            if current is self._start:
                break

        # Insere p apos o no que minimiza o aumento
        node.next = best_node.next
        best_node.next = node
