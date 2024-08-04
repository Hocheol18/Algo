from collections import deque

def solution(maps):
    queue = deque()
    n, m = len(maps), len(maps[0])
    boundary = lambda y,x : y>=0 and x>=0 and x<m and y<n
    direction = [(1,0), (0,1), (-1,0), (0, -1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    queue.append([1, 0, 0])
    
    while queue:
        dis, y, x = queue.popleft()
        
        if (y == n-1) and (x == m-1):
            return dis
        
        for dy, dx in direction:
            if boundary(y+dy, x+dx):
                if (maps[y+dy][x+dx] == 1) and (not visited[y+dy][x+dx]):
                    visited[y+dy][x+dx] = True
                    queue.append([dis+1, y+dy, x+dx])

    return -1