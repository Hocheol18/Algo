import heapq

def solution(N, road, K):
    queue = []
    graph = [[] for _ in range(N+1)]
    dis = [1e9 for _ in range(N+1)]
    dis[1] = 0

    for i in road:
        graph[i[0]].append([i[1], i[2]])
        graph[i[1]].append([i[0], i[2]])

    heapq.heappush(queue, (0, 1))

    while queue:
        cur_dis, cur_node = heapq.heappop(queue)

        ## 핵심 >>
        # 만약 이미 방문한 노드라면, continue
        if cur_dis > dis[cur_node]:
            continue

        for nxt, nxt_dis in graph[cur_node]:
            if (dis[nxt] > nxt_dis + dis[cur_node]) & (nxt_dis + dis[cur_node] <= K):
                dis[nxt] = nxt_dis + dis[cur_node]
                heapq.heappush(queue, [dis[nxt], nxt])

    return sum(1 for _ in dis if _ < 1e9)