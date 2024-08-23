from collections import deque

def bfs(y, x, land, label):
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True
    land[y][x] = label
    cnt = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            if boundary(y+dy, x+dx) and not visited[y+dy][x+dx] and land[y+dy][x+dx] == 1:
                land[y+dy][x+dx] = label
                visited[y+dy][x+dx] = True
                queue.append([y+dy, x+dx])
                cnt += 1

    return cnt

def solution(land):
    global boundary, direction, visited

    answer = 0
    n, m = len(land), len(land[0])
    boundary = lambda y, x: 0 <= y < n and 0 <= x < m
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    label = 2
    size_map = {}

    for y in range(n):
        for x in range(m):
            if not visited[y][x] and land[y][x] == 1:
                size = bfs(y, x, land, label)
                size_map[label] = size
                label += 1

    for x in range(m):
        check = []
        ans = 0
        for y in range(n):
            if land[y][x] not in check:
                if land[y][x] >= 2:
                    ans += size_map[land[y][x]]
                    check.append(land[y][x])

        answer  = max(ans, answer)

    return answer