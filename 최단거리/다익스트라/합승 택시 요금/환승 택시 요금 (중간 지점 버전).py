import heapq

def dijkstra(n, start, edges):
    dis = [1e9] * (n + 1)
    dis[start] = 0
    queue = [(0, start)]
    while queue:
        current_dis, node = heapq.heappop(queue)
        if current_dis > dis[node]:
            continue
        for cur_node in edges[node]:
            u, v, w = cur_node
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, (dis[v], v))
    return dis

def solution(n, s, a, b, fares):
    edges = [[] for _ in range(n + 1)]
    
    for fare in fares:
        u, v, w = fare
        edges[u].append((u, v, w))
        edges[v].append((v, u, w))
        
    dis_from_s = dijkstra(n, s, edges)
    dis_from_a = dijkstra(n, a, edges)
    dis_from_b = dijkstra(n, b, edges)
    
    answer = dis_from_s[a] + dis_from_s[b]
    
    for i in range(1, n + 1):
        if dis_from_s[i] != 1e9 and dis_from_a[i] != 1e9 and dis_from_b[i] != 1e9:
            answer = min(answer, dis_from_s[i] + dis_from_a[i] + dis_from_b[i])
    
    return answer