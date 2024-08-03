import sys

def bellman_ford(n, edges, start):
    dis = [1e9] * (n + 1)
    dis[start] = 0

    # (n-1)번 반복하여 모든 간선을 완화
    # 마지막 한 번 더 사이클을 돌면서 한 번 더 최소값이 갱신되면, 음수인 싸이클 존재
    for i in range(n):
        for u, v, w in edges:
            if dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                if i == n-1:
                    return False

    # # 음수 사이클 체크: 출발점에서 도달할 수 있는 정점에서 음수 사이클 확인
    # for u, v, w in edges:
    #     if dis[u] + w < dis[v]:
    #         return False  # 음수 사이클 존재

    return True

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):    
        ms, me, mt = map(int, sys.stdin.readline().split())
        edges.append((ms, me, -abs(mt)))

    has_negative_cycle = False
    if not bellman_ford(n, edges, 1):
        has_negative_cycle = True
        
    if has_negative_cycle:
        print("YES")
    else:
        print("NO")