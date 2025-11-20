
import math
import heapq

INF = float("inf")

def dijkstra_matrix(graph, source):
    n = len(graph)
    dist = [INF] * n
    visited = [False] * n
    dist[source] = 0
    for _ in range(n):
        u = -1
        min_dist = INF
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if graph[u][v] != 0:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
    return dist

def dijkstra_list(graph, source):
    n = len(graph)
    dist = [INF] * n
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        cd, u = heapq.heappop(pq)
        if cd > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def bellman_ford_matrix(graph, source):
    n = len(graph)
    dist = [INF] * n
    dist[source] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != 0:
                    if dist[u] + graph[u][v] < dist[v]:
                        dist[v] = dist[u] + graph[u][v]
    return dist

def bellman_ford_list(graph, source):
    n = len(graph)
    dist = [INF] * n
    dist[source] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist
