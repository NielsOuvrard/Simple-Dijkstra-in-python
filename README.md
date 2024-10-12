# The dijkstra algorithm

## A little bit of context

It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later, in 1959 in the academic journal "**Numerische Mathematik**".

The algorithm exists in many variants; Dijkstra's original variant found **the shortest path between two nodes**, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

The algorithm works by keeping track of the currently known shortest distance from each node to the source node and iteratively exploring the vertices of the graph.

## Exercice 1

![Dijkstra_Excersise_1](exercices/Dijkstra_Excersise_1.JPG)

```python
Node A:
Distances: {'A': 0, 'B': 3, 'C': 5, 'D': 4}
Nodes visited: {'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B']}

Node B:
Distances: {'A': 3, 'B': 0, 'C': 3, 'D': 1}
Nodes visited: {'A': ['B'], 'B': [], 'C': ['B', 'D'], 'D': ['B']}

Node C:
Distances: {'A': 5, 'B': 3, 'C': 0, 'D': 2}
Nodes visited: {'A': ['C'], 'B': ['C', 'D'], 'C': [], 'D': ['C']}

Node D:
Distances: {'A': 4, 'B': 1, 'C': 2, 'D': 0}
Nodes visited: {'A': ['B'], 'B': ['D'], 'C': ['D'], 'D': []}
```

## Exercice 2

![Dijkstra_Excersise_2](exercices/Dijkstra_Excersise_2.JPG)

```python
Node A:
Distances: {'A': 0, 'B': 5, 'C': 7, 'D': 7}
Nodes visited: {'A': [], 'B': ['A'], 'C': ['A', 'B'], 'D': ['B']}

Node B:
Distances: {'A': 5, 'B': 0, 'C': 2, 'D': 2}
Nodes visited: {'A': ['B'], 'B': [], 'C': ['B'], 'D': ['B']}

Node C:
Distances: {'A': 7, 'B': 2, 'C': 0, 'D': 4}
Nodes visited: {'A': ['C', 'B'], 'B': ['C'], 'C': [], 'D': ['C', 'B']}

Node D:
Distances: {'A': 7, 'B': 2, 'C': 4, 'D': 0}
Nodes visited: {'A': ['B'], 'B': ['D'], 'C': ['D', 'B'], 'D': []}
```

## Exercice 3

![Dijkstra_Excersise_3](exercices/Dijkstra_Excersise_3.JPG)

```python
Node A:
Distances: {'A': 0, 'B': 2, 'C': 3, 'D': 6, 'E': 4, 'F': 6}
Nodes visited: {'A': [], 'B': ['A'], 'C': ['A', 'B'], 'D': ['B'], 'E': ['B'], 'F': ['E']}

Node B:
Distances: {'A': 5, 'B': 0, 'C': 1, 'D': 4, 'E': 2, 'F': 4}
Nodes visited: {'A': ['C'], 'B': [], 'C': ['B'], 'D': ['B'], 'E': ['B'], 'F': ['E']}

Node C:
Distances: {'A': 4, 'B': 1, 'C': 0, 'D': 5, 'E': 3, 'F': 5}
Nodes visited: {'A': ['C'], 'B': ['C'], 'C': [], 'D': ['B'], 'E': ['C'], 'F': ['E']}

Node D:
Distances: {'A': 9, 'B': 4, 'C': 5, 'D': 0, 'E': 3, 'F': 2}
Nodes visited: {'A': ['C'], 'B': ['D'], 'C': ['E', 'B'], 'D': [], 'E': ['D'], 'F': ['D']}

Node E:
Distances: {'A': 7, 'B': 2, 'C': 3, 'D': 3, 'E': 0, 'F': 2}
Nodes visited: {'A': ['C'], 'B': ['E'], 'C': ['E'], 'D': ['E'], 'E': [], 'F': ['E']}

Node F:
Distances: {'A': 9, 'B': 4, 'C': 5, 'D': 2, 'E': 2, 'F': 0}
Nodes visited: {'A': ['C'], 'B': ['D', 'E'], 'C': ['E'], 'D': ['F'], 'E': ['F'], 'F': []}
```

## Exercice 4

![Dijkstra_Excersise_4](exercices/Dijkstra_Excersise_4.JPG)

```python
Node A:
Distances: {'A': 0, 'B': 10, 'C': 2, 'D': 7, 'E': 10, 'F': 14, 'G': 13, 'H': 11}
Nodes visited: {'A': [], 'B': ['A'], 'C': ['A'], 'D': ['C'], 'E': ['D'], 'F': ['E'], 'G': ['H'], 'H': ['B']}

Node B:
Distances: {'A': 10, 'B': 0, 'C': 12, 'D': 11, 'E': 8, 'F': 4, 'G': 3, 'H': 1}
Nodes visited: {'A': ['B'], 'B': [], 'C': ['A'], 'D': ['E'], 'E': ['F'], 'F': ['G'], 'G': ['H'], 'H': ['B']}

Node C:
Distances: {'A': 2, 'B': 12, 'C': 0, 'D': 5, 'E': 8, 'F': 12, 'G': 13, 'H': 13}
Nodes visited: {'A': ['C'], 'B': ['A'], 'C': [], 'D': ['C'], 'E': ['D'], 'F': ['E'], 'G': ['F'], 'H': ['B']}

Node D:
Distances: {'A': 7, 'B': 11, 'C': 5, 'D': 0, 'E': 3, 'F': 7, 'G': 8, 'H': 10}
Nodes visited: {'A': ['C'], 'B': ['A', 'H'], 'C': ['D'], 'D': [], 'E': ['D'], 'F': ['E'], 'G': ['F'], 'H': ['G']}

Node E:
Distances: {'A': 10, 'B': 8, 'C': 8, 'D': 3, 'E': 0, 'F': 4, 'G': 5, 'H': 7}
Nodes visited: {'A': ['B', 'C'], 'B': ['H'], 'C': ['D'], 'D': ['E'], 'E': [], 'F': ['E'], 'G': ['F'], 'H': ['G']}

Node F:
Distances: {'A': 14, 'B': 4, 'C': 12, 'D': 7, 'E': 4, 'F': 0, 'G': 1, 'H': 3}
Nodes visited: {'A': ['B'], 'B': ['H'], 'C': ['D'], 'D': ['E'], 'E': ['F'], 'F': [], 'G': ['F'], 'H': ['G']}

Node G:
Distances: {'A': 13, 'B': 3, 'C': 13, 'D': 8, 'E': 5, 'F': 1, 'G': 0, 'H': 2}
Nodes visited: {'A': ['B'], 'B': ['H'], 'C': ['D'], 'D': ['E'], 'E': ['F'], 'F': ['G'], 'G': [], 'H': ['G']}

Node H:
Distances: {'A': 11, 'B': 1, 'C': 13, 'D': 10, 'E': 7, 'F': 3, 'G': 2, 'H': 0}
Nodes visited: {'A': ['B'], 'B': ['H'], 'C': ['D', 'A'], 'D': ['E'], 'E': ['F'], 'F': ['G'], 'G': ['H'], 'H': []}
```
