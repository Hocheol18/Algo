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

    boolean = bellman_ford(n, edges, 1)
        
    if boolean:
        print("NO")
    else:
        print("YES")