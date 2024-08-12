import sys
import heapq

def cal(a):
    fi_a, fi_b, fi_c = graph[a]

    node_ = 0
    min_dis = 2e9 + 2

    for node in range(1, n+1):
        if visited[node]:
            continue
        se_a, se_b, se_c = graph[node]

        min_dis_cal = min(abs(fi_a - se_a), abs(fi_b - se_b), abs(fi_c - se_c))
        
        if min_dis > min_dis_cal:
            min_dis = min_dis_cal
            node_ = node

    return (0, 0) if node_ == 0 and min_dis == 2e9 + 2 else (min_dis, node_)
    
n = int(sys.stdin.readline())
queue = [(0, 1)]
edges = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
graph = [(0,0,0)]
dis = 0

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append([a,b,c])

while queue:
    wei, node = heapq.heappop(queue)

    if visited[node]:
        continue

    visited[node] = True
    dis += wei

    min_dis, node_ = cal(node)

    if node_ == 0 and min_dis == 0:
        break

    heapq.heappush(queue, [min_dis, node_])

print(dis)