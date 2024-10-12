import sys

def dfs(total, now, answer):
    global ans
    if now > total:
        return
    
    ans = max(ans, answer)
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(total, now + test[i][0], answer + test[i][1])
            visited[i] = False
    
N, T = map(int, sys.stdin.readline().split())
visited = [False for _ in range(N)]
ans = 0
test = []
for _ in range(N):
    test.append(list(map(int, sys.stdin.readline().split())))
dfs(T, 0, 0)
print(ans)