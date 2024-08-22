from collections import deque
from copy import deepcopy

def bfs(ry, rx, by, bx, maze):
    queue = deque()
    r_visited = [[False for _ in range(m)] for _ in range(n)]
    b_visited = [[False for _ in range(m)] for _ in range(n)]
    rr_visited = [[False for _ in range(m)] for _ in range(n)]
    bb_visited = [[False for _ in range(m)] for _ in range(n)]
    r_visited[ry][rx], b_visited[by][bx], rr_visited[ry][rx], bb_visited[by][bx] = True, True, True, True
    queue.append([0, ry, rx, by, bx, deepcopy(r_visited), deepcopy(b_visited), deepcopy(rr_visited), deepcopy(bb_visited)])

    while queue:
        cnt, ry, rx, by, bx, r_visited, b_visited, rr_visited, bb_visited = queue.popleft()
        
        if maze[ry][rx] == 3 and maze[by][bx] == 4:
            return cnt
        
        for dy, dx in direction:
            if maze[ry][rx] == 3:
                if boundary(by+dy, bx+dx) and not b_visited[by+dy][bx+dx] and not ((ry == by+dy) and (rx == bx+dx)) and maze[by+dy][bx+dx] != 5 :
                    b_visited[by+dy][bx+dx] = True
                    queue.append([cnt + 1, ry, rx, by+dy, bx+dx, deepcopy(r_visited), deepcopy(b_visited), deepcopy(rr_visited), deepcopy(bb_visited)])
                if boundary(by+dy, bx+dx) and not bb_visited[by+dy][bx+dx] and not ((ry == by+dy) and (rx == bx+dx)) and maze[by+dy][bx+dx] != 5 :
                    bb_visited[by+dy][bx+dx] = True
                    queue.append([cnt + 1, ry, rx, by+dy, bx+dx, deepcopy(r_visited), deepcopy(b_visited), deepcopy(rr_visited), deepcopy(bb_visited)])

            elif maze[by][bx] == 4:
                if boundary(ry+dy, rx+dx) and not r_visited[ry+dy][rx+dx] and not ((ry+dy == by) and (rx+dx == bx)) and maze[ry+dy][rx+dx] != 5:
                    r_visited[ry+dy][rx+dx] = True
                    queue.append([cnt + 1, ry+dy, rx+dx, by, bx, deepcopy(r_visited), deepcopy(b_visited), deepcopy(rr_visited), deepcopy(bb_visited)])
                if boundary(ry+dy, rx+dx) and not rr_visited[ry+dy][rx+dx] and not ((ry+dy == by) and (rx+dx == bx)) and maze[ry+dy][rx+dx] != 5:
                    rr_visited[ry+dy][rx+dx] = True
                    queue.append([cnt + 1, ry+dy, rx+dx, by, bx, deepcopy(r_visited), deepcopy(b_visited), deepcopy(rr_visited), deepcopy(bb_visited)])
            
            else:
                if boundary(ry+dy, rx+dx) and not r_visited[ry+dy][rx+dx] and maze[ry+dy][rx+dx] != 5:

                    for ddy, ddx in direction:
                        if boundary(by+ddy, bx+ddx) and not b_visited[by+ddy][bx+ddx] and not ((ry+dy == by+ddy) and (rx+dx == bx+ddx)) and maze[by+ddy][bx+ddx] != 5:

                            if (by+ddy == ry and bx+ddx == rx) and (ry+dy == by and rx+dx == bx):
                                continue
                            r_visited[ry+dy][rx+dx] = True  
                            b_visited[by+ddy][bx+ddx] = True
                            queue.append([cnt + 1, ry+dy, rx+dx, by+ddy, bx+ddx, deepcopy(r_visited), deepcopy(b_visited), deepcopy(rr_visited), deepcopy(bb_visited)])
                
                if boundary(by+dy, bx+dx) and not bb_visited[by+dy][bx+dx] and maze[by+dy][bx+dx] != 5:

                    for ddy, ddx in direction:
                        if boundary(ry+ddy, rx+ddx) and not rr_visited[ry+ddy][rx+ddx] and not ((ry+ddy == by+dy) and (rx+ddx == bx+dx)) and maze[ry+ddy][rx+ddx] != 5:
                            if (ry+ddy == by and rx + ddx == bx) and (by+dy == ry and bx+dx == rx):
                                continue 
                            bb_visited[by+dy][bx+dx] = True
                            rr_visited[ry+ddy][rx+ddx] = True
                            queue.append([cnt + 1, ry+ddy, rx+ddx, by+dy, bx+dx, deepcopy(r_visited), deepcopy(b_visited), deepcopy(rr_visited), deepcopy(bb_visited)])

    return 0


def solution(maze):
    global boundary, direction, n, m
    n, m = len(maze), len(maze[0])

    boundary = lambda y,x : y>=0 and x>=0 and y < n and x < m
    direction = [(1,0), (0,1), (-1,0), (0, -1)]
    ry, rx, by, bx = 0, 0, 0, 0

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                ry, rx = y, x
            elif maze[y][x] == 2:
                by, bx = y, x
    ans = bfs(ry, rx, by, bx, maze)
    return ans