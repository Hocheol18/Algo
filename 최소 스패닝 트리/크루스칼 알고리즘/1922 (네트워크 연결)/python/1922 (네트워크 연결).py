import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

rank = [1 for _ in range(n+1)]
par = [i for i in range(n+1)]
graph = []

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
        elif rank[b] > rank[a]:
            par[a] = b
        else:
            par[a] = b
            rank[b] += 1

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append([c,a,b])

graph.sort()

edge, answer = 0, 0

for element in graph:
    wei, prv, nxt = element

    if _find(prv) != _find(nxt):
        _union(prv, nxt)
        edge += 1
        answer += wei

        if edge == n-1:
            break

print(answer)



