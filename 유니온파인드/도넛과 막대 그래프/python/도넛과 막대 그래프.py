par = [i for i in range(1000001)]
rank = [1 for _ in range(1000001)]
edge_ = [1 for _ in range(1000001)]

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
    
    if rank[a] == rank[b]:
        edge_[b] += edge_[a]
        par[a] = b
        rank[b] += 1
    elif rank[a] > rank[b]:
        edge_[a] += edge_[b]
        par[b] = a
    else:
        par[a] = b
        edge_[b] += edge_[a]
        
def solution(edges):
    global answer, answer_
    start = edges[0][0]
    answer = [edges[0][0], 0, 0, 0]
    answer_ = []
    
    for edge in edges:
        if edge[0] != start:
            _union(edge[0], edge[1])
        else:
            answer_.append(edge[1])
            
    for ans in answer_:
        if edge_[_find(ans)] - 1 == rank[_find(ans)] * 2 + 2:
            answer[3] += 1
        elif edge_[_find(ans)] - 1 == rank[_find(ans)] - 1:
            answer[2] += 1
        elif edge_[_find(ans)] - 1 == rank[_find(ans)]:
            answer[1] += 1
        elif edge_[_find(ans)] - 1 == 0:
            answer[2] += 1
        elif edge_[_find(ans)] - 1 == 1:
            answer[1] += 1
            
    return answer