import sys

def bellman_ford(n, graph):
    # 초기화
    dis = [1e9] * (n + 1)
    dis[1] = 0

    # (n-1)번 반복하여 모든 간선을 체크함
    for _ in range(n - 1):
        for u, v, w in graph:
            # 한 번 다녀간 노드는 체크하지 않음. 즉 1e9면 다시 체크 X
            if dis[u] != 1e9 and dis[u] + w < dis[v]:
                dis[v] = dis[u] + w

    # 음수 사이클 체크
    # 한 번 더 체크했을 때 다시 갱신된다면, 음수인 싸이클이 존재함.
    for u, v, w in graph:
        if dis[u] != 1e9 and dis[u] + w < dis[v]:
            print(-1)
            return

    return dis

n, m = map(int, sys.stdin.readline().split())
graph = []

# 단방향 간선이므로
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))

result = bellman_ford(n, graph)

if result:
    for i in range(2, n + 1):
        if result[i] == 1e9:
            print("-1", end="\n")
        else:
            print(result[i], end="\n")