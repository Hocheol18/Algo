import sys

par = [i for i in range(1000001)]
rank = [1 for _ in range(1000001)]

def _find(a):
    if par[a] == a:
        return a
    
    else:
        par[a] = _find(par[a])
        return par[a]

def _union(a, b):
    a = _find(a)
    b = _find(b)

    if a == b:
        return
    
    if rank[a] == rank[b]:
        par[a] = b
        rank[b] += 1
    elif rank[a] > rank[b]:
        par[b] = a
    else:
        par[a] = b


n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        _union(b, c)

    elif a == 1:
        if _find(b) == _find(c):
            print("YES")
        else:
            print("NO")