import heapq

def dj(queue, dis, edges):
    while queue:
        _, node = heapq.heappop(queue)
        for cur_node in edges[node]:
            u, v, w = cur_node
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, [dis[v], v])
            
def solution(n, s, a, b, fares):
    edges = [[] for _ in range(n+1)]
    queue = []
    dis = [1e9 for _ in range(n+1)]
    dis[s] = 0
    
    for fare in fares:
        edges[fare[0]].append([fare[0], fare[1], fare[2]])
        edges[fare[1]].append([fare[1], fare[0], fare[2]])
        
    heapq.heappush(queue, (0, s))
    dj(queue, dis, edges)
    
    answer = dis[a] + dis[b]
    
    for start in range(1, n+1):
        dis_2 = [1e9 for _ in range(n+1)]
        dis_2[start] = 0
        heapq.heappush(queue, (0,start))
        
        dj(queue, dis_2, edges)
        
        if dis_2[a] + dis_2[b] + dis[start] < answer:
            answer = dis_2[a] + dis_2[b] + dis[start]

    return answer