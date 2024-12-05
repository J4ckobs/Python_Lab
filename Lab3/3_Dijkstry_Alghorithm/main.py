"""
from pythonds.graphs import Graph


def add_both_edges(g, key1, key2):
    g.addEdge(key1, key2)
    g.addEdge(key2, key1)


g = Graph()
add_both_edges(g,"Mary", "Sam")
add_both_edges(g, "Mary", "Tom")
add_both_edges(g, "Marry", "Joe")
add_both_edges(g, "Joe", "Tom")

g.addVertex("Sally")

for from_id in g.getVertices():
    t = tuple(v.id for v in g.getVertex(from_id).connectedTo.keys())
    print(f"edge: {from_id} to : {t}")
"""

import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == end:
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    path, current_vertex = [], end
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    if path:
        path.insert(0, current_vertex)

    return distances[end], path

# Przykładowy graf reprezentowany jako słownik
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {'A': 5, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 2},
    'D': {'B': 5, 'C': 2}
}

start_vertex = 'A'
end_vertex = 'D'
distance, path = dijkstra(graph, start_vertex, end_vertex)

print(f"Najkrótsza odległość od {start_vertex} do {end_vertex}: {distance}")
print(f"Ścieżka: {' -> '.join(path)}")
