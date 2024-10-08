def solution(n, results):
    answer, dis = 0, [[1e9 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n + 1):
        dis[i][i] = 0
        
    for result in results:
        dis[result[0]][result[1]] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            # 승리 또는 패배 관계가 있는 경우
            if dis[i][j] != 1e9 or dis[j][i] != 1e9:  
                count += 1
        # 자신을 제외한 모든 선수와의 관계가 명확할 경우
        if count == n:
            answer += 1
                    
    return answer