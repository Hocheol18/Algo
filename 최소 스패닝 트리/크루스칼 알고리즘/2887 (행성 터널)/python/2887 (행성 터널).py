import sys
import heapq

## 핵심 로직
## 현재 노드에 연결된 인접한 노드들과의 간선을 모두 추가함
def add_edges(node, graph, visited, edges):
    for dim in range(3):
        for neighbor in graph[dim][node]:
            if not visited[neighbor[1]]:
                heapq.heappush(edges, neighbor)

n = int(sys.stdin.readline())
points = []

# 각 좌표 입력 받기
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    points.append((x, y, z, i + 1))

# 축 별로 정렬함
x_sorted = sorted(points, key=lambda p: p[0])
y_sorted = sorted(points, key=lambda p: p[1])
z_sorted = sorted(points, key=lambda p: p[2])

# 그래프의 간선을 축별로 인접한 노드들 간에 추가
graph = [{} for _ in range(3)]
for i in range(n - 1):
    # x 축 기준 인접 노드 연결
    d = abs(x_sorted[i][0] - x_sorted[i + 1][0])
    a, b = x_sorted[i][3], x_sorted[i + 1][3]
    graph[0][a] = graph[0].get(a, []) + [(d, b)]
    graph[0][b] = graph[0].get(b, []) + [(d, a)]
    
    # y 축 기준 인접 노드 연결
    d = abs(y_sorted[i][1] - y_sorted[i + 1][1])
    a, b = y_sorted[i][3], y_sorted[i + 1][3]
    graph[1][a] = graph[1].get(a, []) + [(d, b)]
    graph[1][b] = graph[1].get(b, []) + [(d, a)]
    
    # z 축 기준 인접 노드 연결
    d = abs(z_sorted[i][2] - z_sorted[i + 1][2])
    a, b = z_sorted[i][3], z_sorted[i + 1][3]
    graph[2][a] = graph[2].get(a, []) + [(d, b)]
    graph[2][b] = graph[2].get(b, []) + [(d, a)]

# Prim 알고리즘을 사용한 최소 스패닝 트리 구성
visited = [False] * (n + 1)
edges = []
mst_cost = 0

# 첫 번째 노드를 임의로 선택하여 시작
visited[1] = True
add_edges(1, graph, visited, edges)

while edges:
    cost, node = heapq.heappop(edges)
    if not visited[node]:
        visited[node] = True
        mst_cost += cost
        add_edges(node, graph, visited, edges)

print(mst_cost)