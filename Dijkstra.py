# python simple Dijkstra

def list_to_nice_string(l):
    return '-' + '-'.join([str(x) for x in l]) + ('-' if l else '')

def dijkstra(graph, start):
    # STEP 1: Create a dictionary with the distances equal to infinity
    # except for the start node, which is 0
    distances = {node: {
            'dist': float('infinity'), 
            'path': []
        } for node in graph}
    distances[start]['dist'] = 0
    
    # STEP 2: Create a list of unvisited nodes
    unvisited = list(graph.keys())

    # STEP 3: Loop until all nodes have been visited
    while unvisited:

        # STEP 4: Select the unvisited node with the smallest distance
        current_node = min(unvisited, key=lambda node: distances[node]['dist'])

        print(('Starting from:' if current_node == start else 'Visiting:'), current_node)
        to_print = ''

        # STEP 5: For the current node, calculate the distance to each neighbor
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node]['dist'] + weight

            # STEP 6: If the distance is shorter than the current distance, update it
            if distance < distances[neighbor]['dist']:
                if distances[neighbor]['dist'] != float('infinity'):
                    to_print += f'Updating distance of {neighbor} from {distances[neighbor]["dist"]} to {distance}\n'
                    to_print += f'\tOld path: {start}{list_to_nice_string(distances[neighbor]["path"])}{neighbor} = {distances[neighbor]["dist"]}\n'
                    to_print += f'\tNew path: {start}{list_to_nice_string(distances[current_node]["path"])}{current_node}-{neighbor} = {distance}\n'
                else:
                    to_print += f'Setting distance of {neighbor} to {distance}\n'
                distances[neighbor]['dist'] = distance
                distances[neighbor]['path'] = distances[current_node]['path'] +\
                    ([current_node] if current_node != start else [])
        
        print(to_print if to_print else 'No changes\n')
        unvisited.remove(current_node)

    return distances




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
        'B': {'C': 1, 'D': 4, 'E': 2, 'A': 2},
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

    print(f'\033[92mGraph {i + 1}:\033[0m')
    for node in nodes:
        print(f'\033[94mNode {node}:\033[0m')
        
        data = dijkstra(graph, node)
        
        print('Results:')
        for element in data:
            path = list_to_nice_string(data[element]["path"])
            print(f'\t{node}-{element}:\tdistance {data[element]["dist"]}\tpath {node}{path}{element}')
        print('\n')

