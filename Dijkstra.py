# python simple Dijkstra

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    nodes_visited = {node: [] for node in graph}
    while unvisited:
        # Find the node with the smallest distance
        current_node = min(unvisited, key=lambda node: distances[node])

        unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                nodes_visited[neighbor].append(current_node)

    return distances, nodes_visited

graphs = [
    {
        'A': {'B': 3, 'C': 5},
        'B': {'A': 3, 'C': 6, 'D': 1},
        'C': {'A': 5, 'B':6, 'D': 2},
        'D': {'B': 1, 'C': 2}
    }, {
        'A': {'B': 5, 'C': 8},
        'B': {'A': 5, 'C': 2, 'D': 2},
        'C': {'A': 8, 'B': 2, 'D': 6},
        'D': {'B': 2, 'C': 6}
    }, {
        'A': {'B': 2, 'C': 4},
        'B': {'C': 1, 'D': 4, 'E': 2},
        'C': {'A': 4, 'B': 1, 'E': 3},
        'D': {'B': 4, 'E': 3, 'F': 2},
        'E': {'B': 2, 'C': 3, 'D': 3, 'F': 2},
        'F': {'D': 2, 'E': 2}
    }, {
        'A': {'B': 10, 'C': 2},
        'B': {'A': 10, 'H': 1},
        'C': {'A': 2, 'D': 5},
        'D': {'C': 5, 'E': 3},
        'E': {'D': 3, 'F': 4},
        'F': {'E': 4, 'G': 1},
        'G': {'F': 1, 'H': 2},
        'H': {'B': 1, 'G': 2}
    }
]

for i, graph in enumerate(graphs):
    nodes = graph.keys()

    print(f'Graph {i + 1}:')
    for node in nodes:
        distances, nodes_visited = dijkstra(graph, node)
        print(f'Node {node}:\nDistances: {distances}\nNodes visited: {nodes_visited}\n')
