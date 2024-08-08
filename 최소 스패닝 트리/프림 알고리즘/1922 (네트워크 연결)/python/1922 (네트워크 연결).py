import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
queue = [[0,1]]

answer = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

while queue:
    dis, node = heapq.heappop(queue)

    if visited[node]:
        continue

    answer += dis
    visited[node] = True

    for nxt, wei in graph[node]:
        if not visited[nxt]:
            heapq.heappush(queue, [wei, nxt])

print(answer)