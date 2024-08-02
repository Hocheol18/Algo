import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dis = [[1e9 for _ in range(n+1)] for _ in range(n+1)]

for i in range(len(dis)):
    for j in range(len(dis[i])):
        if i == j:
            dis[i][j] = 0

# 거리 정보를 전부 소요값으로 변경
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if dis[a][b] > c:
        dis[a][b] = c

# 거쳐가는 노드 (기준 노드)
for k in range(1, n + 1):
    # i : 출발 노드
    for i in range(1, n + 1):
        # j : 도착 노드
        for j in range(1, n + 1):
            # i에서 j로 가는 최소 비용 VS (i에서 k로 가는 최소비용 + 노드 k에서 j로 가는 비용)
            # 기준 노드를 거쳐 가는 게 더 빠르다면, 그걸로 교체
            if dis[i][j] > dis[i][k] + dis[k][j]:
                dis[i][j] = dis[i][k] + dis[k][j]
        
for i in range(1, len(dis)):
    for j in range(1, len(dis[i])):
        if dis[i][j] < 1e9:
            print(dis[i][j], end=" ")
        else:
            print(0, end=" ")
    print("")