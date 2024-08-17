def do(reqs, first):
    time = 0
    stack = [[] for _ in range(5)]
    while reqs:
        a, b, c = reqs.pop(0)
        if first[c-1] != 0:
            first[c-1] -= 1

        else:
            stack[c-1].append([a,b,c])

def combi(depth, n, k, first, vis, reqs):
    if depth == k:
        if n == 0:
            do(reqs, first)
        return
    
    for nxt in range(n+1):
        if n-nxt < 0:
            continue
        if not vis[depth]:
            vis[depth] = True
            first[depth] += nxt
            combi(depth+1, n-nxt, k, first, vis, reqs)
            first[depth] -= nxt
            vis[depth] = False

def solution(k, n, reqs):
    first = [1 for _ in range(k)]
    n -= k
    vis = [False for _ in range(k)]
    combi(0, n, k, first, vis, reqs)