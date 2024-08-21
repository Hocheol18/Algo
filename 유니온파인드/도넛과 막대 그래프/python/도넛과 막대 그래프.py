par = [i for i in range(1000000)]
rank = [1 for _ in range(1000000)]
edge_ = [0 for _ in range(1000000)]
node_ = [0 for _ in range(1000000)]

def _find(a):
    if par[a] == a:
        return a
    par[a] = _find(par[a])
    return par[a]

def _union(a, b):
    a = _find(a)
    b = _find(b)
    
    if a == b:
        edge_[a] += 1
        return
    
    if rank[a] < rank[b]:
        a, b = b, a

    par[b] = a
    edge_[a] += edge_[b] + 1
    node_[a] += node_[b] + 1
    
    if rank[a] == rank[b]:
        rank[a] += 1
        
def solution(edges):
    # 출발 노드 구하는 로직
    connection_count = [0] * 1000000
    for u, v in edges:
        connection_count[u] += 1
        connection_count[v] =- 1
    start_node = connection_count.index(max(connection_count))
    answer = [start_node, 0, 0, 0]
    
    box = []
    
    for u, v in edges:
        if u == start_node:
            node_[v] += 1
            box.append(v)

    for u, v in edges:
        if u != start_node:
            _union(u,v)
            
    for element in box:
        target = _find(element)
        if node_[target] == edge_[target] + 1:
            answer[2] += 1
        elif node_[target] == edge_[target]:
            answer[1] += 1
        elif node_[target] + 1 == edge_[target]:
            answer[3] += 1 
    
    return answer