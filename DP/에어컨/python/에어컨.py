def solution(temperature, t1, t2, a, b, onboard):
    MIN_TEMP, MAX_TEMP = -10, 40
    OFFSET = 10  
    dp = [[float('inf') for _ in range(MAX_TEMP - MIN_TEMP + 1)] for _ in range(len(onboard))]
    
    dp[0][temperature + OFFSET] = 0
    for i in range(1, len(onboard)):
        # 탑승 중일 때는, 무조건 t1 - t2 사이의 온도
        if onboard[i]:
            start, end = t1, t2
        # 그렇지 않을 경우에는 모든 경우 생각
        else:
            start, end = MIN_TEMP, MAX_TEMP
        
        for j in range(start, end + 1):
            curr_temp = j + OFFSET
            prev_temp = temperature + OFFSET
            # 이전 온도와 현재 온도의 관계에 따라 비용 계산
            costs = [float('inf'), float('inf'), float('inf')]
            
            # 범위 계산, edge 케이스를 생각해서 작성해주어야 한다.
            if 0 <= curr_temp - 1 < len(dp[0]):
                costs[0] = dp[i-1][curr_temp - 1] + (a if curr_temp > prev_temp else 0)
            
            if 0 <= curr_temp < len(dp[0]):
                costs[1] = dp[i-1][curr_temp] + (b if curr_temp != prev_temp else 0)
            
            if 0 <= curr_temp + 1 < len(dp[0]):
                costs[2] = dp[i-1][curr_temp + 1] + (a if curr_temp < prev_temp else 0)
            
            dp[i][curr_temp] = min(costs)
            
    return min(dp[-1])