import sys

def dijkstra(graph, start):
    shortest_distance = {}
    shortest_path = {}
    for node in graph:
        shortest_distance[node] = float('inf')
    shortest_distance[start] = 0
    shortest_path[start] = []

    while graph:
        min_node = None
        for node in graph:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        current_distance = shortest_distance[min_node]
        for neighbor, weight in graph[min_node].items():
            distance = current_distance + weight
            if distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance
                shortest_path[neighbor] = shortest_path[min_node] + [min_node]

        del graph[min_node]

    return shortest_distance, shortest_path

# Kasus Terburuk (Worst Case)
graph = {
    'A': {'B': 1, 'C': 1, 'D': 1, 'E': 1},
    'B': {'A': 1, 'C': 1, 'D': 1, 'E': 1},
    'C': {'A': 1, 'B': 1, 'D': 1, 'E': 1},
    'D': {'A': 1, 'B': 1, 'C': 1, 'E': 1},
    'E': {'A': 1, 'B': 1, 'C': 1, 'D': 1}
}

start_node = 'A'
distances, paths = dijkstra(graph, start_node)

print("Shortest distances:")
for node, distance in distances.items():
    print(f"To node {node}: {distance}")

print("Shortest paths:")
for node, path in paths.items():
    print(f"To node {node}: {' -> '.join(path + [node])}")