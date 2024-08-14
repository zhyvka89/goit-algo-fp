import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))

    return dist

# Приклад використання
graph = [
    [(1, 1), (2, 4)],
    [(0, 1), (2, 2), (3, 5)],
    [(0, 4), (1, 2), (3, 1)],
    [(1, 5), (2, 1)]
]

start_vertex = 0
distances = dijkstra(graph, start_vertex)
print("Найкоротші відстані від вершини", start_vertex, "до всіх інших вершин:", distances)