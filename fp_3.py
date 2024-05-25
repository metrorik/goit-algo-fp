import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # якщо граф неорієнтований

def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як безкінечних
    distances = {vertex: float('infinity') for vertex in graph.graph}
    distances[start] = 0

    # Створення пріоритетної черги
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропуск обробки вершини, якщо знайдена довша відстань
        if current_distance > distances[current_vertex]:
            continue

        # Перевірка суміжних вершин
        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда, оновити відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
vertices = 9
g = Graph(vertices)

edges = [
    (0, 1, 4), (0, 7, 8),
    (1, 2, 8), (1, 7, 11),
    (2, 3, 7), (2, 8, 2), (2, 5, 4),
    (3, 4, 9), (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1), (6, 8, 6),
    (7, 8, 7)
]

for u, v, w in edges:
    g.add_edge(u, v, w)

start_vertex = 0
distances = dijkstra(g, start_vertex)

print("Відстані від початкової вершини до всіх інших вершин:")
for vertex in range(vertices):
    print(f"Відстань до вершини {vertex}: {distances[vertex]}")
