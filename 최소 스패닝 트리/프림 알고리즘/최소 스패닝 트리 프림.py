import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([a,b,c])
    graph[b].append([b,a,c])

for i in graph:
    i.sort(key=lambda x : x[2])

answer = 0
queue = [(0,1)]

while queue:
    weight, node = heapq.heappop(queue)

    if visited[node]:
        continue

    answer += weight
    visited[node] = True

    for prv, nxt, wei in graph[node]:
        if not visited[nxt]:
            heapq.heappush(queue, [wei, nxt])

print(answer)
