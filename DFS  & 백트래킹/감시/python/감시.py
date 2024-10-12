import copy

def logic(y, x, dy, dx):
    while True:
        if not boundary(y+dy, x+dx):
            break

        elif b[y+dy][x+dx] == 6:
            break

        if b[y+dy][x+dx] == 0:
            b[y+dy][x+dx] = 9

        y, x = y+dy, x+dx

def dfs(target, cctv, now):
    global b, ans
    if now == target:
        answer = sum(row.count(0) for row in b)
        ans = min(ans, answer)
        return

    cc = cctv[now]
    original_b = [row[:] for row in b]
    
    if b[cc[0]][cc[1]] == 1:
        for i in range(1, 5):
            logic(cc[0], cc[1], direction[i][0], direction[i][1])
            dfs(target, cctv, now + 1)
            b = [row[:] for row in original_b]
    elif b[cc[0]][cc[1]] == 2:
        logic(cc[0], cc[1], direction[1][0], direction[1][1])
        logic(cc[0], cc[1], direction[2][0], direction[2][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]
        logic(cc[0], cc[1], direction[3][0], direction[3][1])
        logic(cc[0], cc[1], direction[4][0], direction[4][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]
    elif b[cc[0]][cc[1]] == 3:
        logic(cc[0], cc[1], direction[1][0], direction[1][1])
        logic(cc[0], cc[1], direction[3][0], direction[3][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]

        logic(cc[0], cc[1], direction[1][0], direction[1][1])
        logic(cc[0], cc[1], direction[4][0], direction[4][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]

        logic(cc[0], cc[1], direction[2][0], direction[2][1])
        logic(cc[0], cc[1], direction[3][0], direction[3][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]

        logic(cc[0], cc[1], direction[2][0], direction[2][1])
        logic(cc[0], cc[1], direction[4][0], direction[4][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]
    elif b[cc[0]][cc[1]] == 4:
        logic(cc[0], cc[1], direction[1][0], direction[1][1])
        logic(cc[0], cc[1], direction[2][0], direction[2][1])
        logic(cc[0], cc[1], direction[3][0], direction[3][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]

        logic(cc[0], cc[1], direction[1][0], direction[1][1])
        logic(cc[0], cc[1], direction[2][0], direction[2][1])
        logic(cc[0], cc[1], direction[4][0], direction[4][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]

        logic(cc[0], cc[1], direction[3][0], direction[3][1])
        logic(cc[0], cc[1], direction[4][0], direction[4][1])
        logic(cc[0], cc[1], direction[1][0], direction[1][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]

        logic(cc[0], cc[1], direction[3][0], direction[3][1])
        logic(cc[0], cc[1], direction[4][0], direction[4][1])
        logic(cc[0], cc[1], direction[2][0], direction[2][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]
    else:
        for i in range(1, 5):
            logic(cc[0], cc[1], direction[i][0], direction[i][1])
        dfs(target, cctv, now + 1)
        b = [row[:] for row in original_b]

n, m = map(int, input().split())

b = []
for _ in range(n):
    b.append(list(map(int, input().split())))

direction = {1 : [1,0], 2 : [-1, 0], 3:[0,1], 4:[0, -1]}
boundary = lambda y, x : y >= 0 and x >= 0 and y < n and x < m
target, ans = 0, 1e9
cctv = []
for i in range(n):
    for j in range(m):
        if b[i][j] != 0 and b[i][j] != 6:
            target += 1
            cctv.append([i,j])

dfs(target, cctv, 0)

print(ans)
