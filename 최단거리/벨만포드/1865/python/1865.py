import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    graph_2 = [[] for _ in range(n+1)]
    for _ in range(m+w):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append([s,e,t])
        graph[e].append([e,s,t])
        ms, me, mt = map(int, sys.stdin.readline().split())
        graph_2[ms].append([ms, me, mt])

    print(graph)
    print(graph_2)