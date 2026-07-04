# Trabalho Prático 4 — TSP com Heurísticas de Inserção

## Descrição

Implementação em **Python** de duas heurísticas de construção de circuito para o **Traveling Salesman Problem (TSP)**:

1. **Nearest Insertion** — insere cidades priorizando a proximidade ao circuito atual;
2. **Smallest Insertion** — insere cidades priorizando o menor aumento no comprimento do circuito.

---

## Heurísticas implementadas

### Nearest Insertion

A cada passo, identifica o nó do circuito atual que está **mais próximo** do novo ponto `p` e insere `p` imediatamente após esse nó.

> Critério de escolha: **proximidade** da cidade ao circuito existente.

### Smallest Insertion

A cada passo, avalia o custo de inserção de `p` em **todas as posições** do circuito atual — ou seja, entre cada par de nós consecutivos — e insere `p` na posição que provoca o **menor aumento** no comprimento total do circuito.

> Critério de escolha: **menor impacto** no comprimento do percurso.

---

## Estrutura do projeto

```
t4-tsp/
├── README.md
├── dados/
│   ├── tsp10.txt               # instância de depuração (10 pontos)
│   ├── tsp10-nearest.txt       # tour de referência — nearest
│   ├── tsp10-smallest.txt      # tour de referência — smallest
│   ├── tsp10-optimal.txt       # tour ótimo de referência
│   └── usa13509.txt            # instância oficial (13 509 pontos)
└── src/
    ├── main.py                 # programa principal
    ├── point.py                # classe Point (ponto 2D)
    ├── tour.py                 # classe Tour com as duas heurísticas
    └── visualizer.py           # visualizador dos circuitos
```

---

## Requisitos

- Python 3.8+
- `matplotlib` (para visualização)

```bash
pip install matplotlib
```

---

## Como executar

Entre na pasta `src/` e execute:

```bash
# Instância de depuração (10 pontos)
python main.py ../dados/tsp10.txt

# Instância oficial (13 509 pontos)
python main.py ../dados/usa13509.txt
```

### Saída esperada (tsp10.txt)

```
Instancia TSP carregada:
- dimensoes: 600 x 600
- numero de pontos: 10

Nearest insertion:  tamanho = 10, comprimento = 1566.1363
Smallest insertion: tamanho = 10, comprimento = 1655.7462
```

A janela gráfica exibe:
- Circuito **nearest** em **vermelho**
- Circuito **smallest** em **azul**
- Pontos da instância em **preto**
- Comprimentos na legenda
