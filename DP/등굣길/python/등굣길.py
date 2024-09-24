def solution(m, n, puddles):
    maps = [[0 for _ in range(m)] for _ in range(n)]
    maps[0][0] = 1
    boundary = lambda y, x : y>=0 and x>=0 and y < n and x < m
    direction = [(0,1), (1,0)]

    for puddle in puddles:
        maps[puddle[1]-1][puddle[0]-1] = -1
    
    for y in range(n):
        for x in range(m):
            if maps[y][x] != -1:
                for dy, dx in direction:
                    if boundary(y+dy, x+dx) and maps[y+dy][x+dx] != -1:
                        maps[y+dy][x+dx] += maps[y][x]
    return maps[-1][-1] % 1000000007