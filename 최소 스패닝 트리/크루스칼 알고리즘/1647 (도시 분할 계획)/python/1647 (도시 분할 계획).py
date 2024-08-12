import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dis = 0
queue = [(0,1)]
max_ = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

for element in graph:
    element.sort(key=lambda x : x[1])

while queue:
    wei, node = heapq.heappop(queue)
 
    if visited[node]:
        continue

    dis += wei
    visited[node] = True
    max_ = max(wei, max_)

    for nxt, weight in graph[node]:
        if not visited[nxt]:
            heapq.heappush(queue, [weight, nxt])

print(dis - max_)