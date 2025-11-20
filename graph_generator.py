
import random
import math

def generate_graph(N, L, R):
    coords = [(random.uniform(0, L), random.uniform(0, L)) for _ in range(N)]
    matrix = [[0]*N for _ in range(N)]
    adj_list = [[] for _ in range(N)]
    for i in range(N):
        x1, y1 = coords[i]
        for j in range(i+1, N):
            x2, y2 = coords[j]
            d = math.dist((x1, y1), (x2, y2))
            if d <= R:
                w = random.randint(1, 100)
                matrix[i][j] = w
                matrix[j][i] = w
                adj_list[i].append((j, w))
                adj_list[j].append((i, w))
    return matrix, adj_list
