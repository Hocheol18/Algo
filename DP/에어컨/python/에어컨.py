def solution(temperature, t1, t2, a, b, onboard):
    dp = [[1e9 for _ in range(80)] for _ in range(len(onboard))]
    dp[0][temperature + 15] = 0

    for i in range(1, len(onboard)):
        start, end = 0, 0
    
        if onboard[i]:
            start, end = t1 + 15, t2 + 15

        else:
            start, end = min(t1, temperature) + 15, max(t2, temperature) + 15

        for j in range(start, end + 1):
            if temperature + 15 > j:
                dp[i][j] = min( dp[i-1][j] + b, dp[i-1][j-1] + 0, dp[i-1][j+1] + a)
            elif temperature + 15 < j:
                dp[i][j] = min(dp[i-1][j-1] + a, dp[i-1][j] + b, dp[i-1][j+1] + 0)
            else:
                dp[i][j] = min(dp[i-1][j-1] + a, dp[i-1][j] + 0, dp[i-1][j+1] + a)
                
    return min(dp[-1])