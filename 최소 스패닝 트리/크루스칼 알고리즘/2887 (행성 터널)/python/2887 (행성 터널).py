# import sys
# import heapq

# def dd(input_graph, index, a, min_dis, node_, node_positions):
#     _, fi_a, fi_b, fi_c = input_graph[index]
#     if not visited[input_graph[index + 1][0]]:
#         _, se_a, se_b, se_c = input_graph[index+1]
#         min_dis_cal = min(abs(fi_a - se_a), abs(fi_b - se_b), abs(fi_c - se_c))

#         if min_dis > min_dis_cal:
#             min_dis = min_dis_cal
#             node_ = input_graph[index + 1][0]
#             node_positions[a] = _

#     if index != 0:
#         if not visited[input_graph[index - 1][0]]:
#             _, se_a, se_b, se_c = input_graph[index-1]
#             min_dis_cal = min(abs(fi_a - se_a), abs(fi_b - se_b), abs(fi_c - se_c))
#             if min_dis > min_dis_cal:
#                 min_dis = min_dis_cal
#                 node_ = input_graph[index - 1][0]
#                 node_positions[a] = _
#     return min_dis, node_

# def cal(a, input_graph, min_dis, node_, node_positions):
#     index = node_positions[a]
#     min_dis, node_ = dd(input_graph, index, a, min_dis, node_, node_positions)
#     return min_dis, node_
    
# n = int(sys.stdin.readline())
# queue = [(0, 1)]
# edges = [[] for _ in range(n+1)]
# visited = [False for _ in range(n+1)]
# graph = [(0, 4e9,4e9,4e9)]
# dis = 0

# for index in range(1, n+1):
#     a, b, c = map(int, sys.stdin.readline().split())
#     graph.append([index, a,b,c])

# x_graph = sorted(graph, key=lambda x : x[1])
# y_graph = sorted(graph, key=lambda x : x[2])
# z_graph = sorted(graph, key=lambda x : x[3])
# x_node_positions = {x[0]: i for i, x in enumerate(x_graph)}
# y_node_positions = {x[0]: i for i, x in enumerate(y_graph)}
# z_node_positions = {x[0]: i for i, x in enumerate(z_graph)}

# while queue:
#     wei, node = heapq.heappop(queue)

#     if visited[node]:
#         continue

#     visited[node] = True
#     dis += wei

#     node_ = 0
#     min_dis = 2e9 + 2

#     min_dis, node_ = cal(node, x_graph, min_dis, node_, x_node_positions)
#     min_dis, node_ = cal(node, y_graph, min_dis, node_, y_node_positions)
#     min_dis, node_ = cal(node, z_graph, min_dis, node_, z_node_positions)

#     if (node_ != 0) and (min_dis != 2e9 + 2):
#         heapq.heappush(queue, [min_dis, node_])

# print(dis)



import sys
import heapq

def add_edges(node, graph, visited, edges):
    # 현재 노드에 연결된 인접한 노드들과의 간선을 모두 추가
    for dim in range(3):
        for neighbor in graph[dim][node]:
            if not visited[neighbor[1]]:
                heapq.heappush(edges, neighbor)

n = int(sys.stdin.readline())
points = []

# 각 좌표 입력 받기
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    points.append((x, y, z, i + 1))

# 각 축별로 정렬
x_sorted = sorted(points, key=lambda p: p[0])
y_sorted = sorted(points, key=lambda p: p[1])
z_sorted = sorted(points, key=lambda p: p[2])

# 그래프의 간선을 축별로 인접한 노드들 간에 추가
graph = [{} for _ in range(3)]
for i in range(n - 1):
    # x 축 기준 인접 노드 연결
    d = abs(x_sorted[i][0] - x_sorted[i + 1][0])
    a, b = x_sorted[i][3], x_sorted[i + 1][3]
    graph[0][a] = graph[0].get(a, []) + [(d, b)]
    graph[0][b] = graph[0].get(b, []) + [(d, a)]
    
    # y 축 기준 인접 노드 연결
    d = abs(y_sorted[i][1] - y_sorted[i + 1][1])
    a, b = y_sorted[i][3], y_sorted[i + 1][3]
    graph[1][a] = graph[1].get(a, []) + [(d, b)]
    graph[1][b] = graph[1].get(b, []) + [(d, a)]
    
    # z 축 기준 인접 노드 연결
    d = abs(z_sorted[i][2] - z_sorted[i + 1][2])
    a, b = z_sorted[i][3], z_sorted[i + 1][3]
    graph[2][a] = graph[2].get(a, []) + [(d, b)]
    graph[2][b] = graph[2].get(b, []) + [(d, a)]

# Prim 알고리즘을 사용한 최소 스패닝 트리 구성
visited = [False] * (n + 1)
edges = []
mst_cost = 0

# 첫 번째 노드를 임의로 선택하여 시작
visited[1] = True
add_edges(1, graph, visited, edges)

while edges:
    cost, node = heapq.heappop(edges)
    if not visited[node]:
        visited[node] = True
        mst_cost += cost
        add_edges(node, graph, visited, edges)

print(mst_cost)