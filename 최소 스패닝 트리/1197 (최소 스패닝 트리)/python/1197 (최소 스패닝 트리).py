### 크루스칼
import sys

# 백존 재귀 오류남 ㅡㅡ 짜증
sys.setrecursionlimit(100000)
v, e = map(int, sys.stdin.readline().split())

par = [i for i in range(v+1)]
rank = [1 for _ in range(v+1)]

# 유니온파인드
def _find(a):
    if par[a] == a:
        return a
    
    par[a] = _find(par[a])
    return par[a]

def _union(a, b):
    a = _find(a)
    b = _find(b)

    if a != b:
        if rank[a] > rank[b]:
            par[b] = a
        elif rank[a] < rank[b]:
            par[a] = b
        else:
            par[b] = a
            rank[a] += 1

graph = []

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append([c,a,b])

graph.sort()

answer = 0
edges = 0

for c, a, b in graph:
    if _find(a) != _find(b):
        _union(a,b)
        answer += c
        edges += 1
        # 최소 스패닝 트리가 완성 되었을 경우 종료
        if edges == v-1: 
            break
    
print(answer)
            

### 프림
