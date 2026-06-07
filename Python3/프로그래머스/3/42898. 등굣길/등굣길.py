def solution(m, n, puddles):
    answer = 0
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    for r in range(n):
        for c in range(m):
            if [c+1, r+1] in puddles:
                continue
            if r == 0 and c == 0:
                continue
            if r == 0:
                dp[r][c] = dp[r][c-1]
            elif c == 0:
                dp[r][c] = dp[r-1][c]
            else:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
            dp[r][c] %= 1000000007
    answer = dp[-1][-1]
    return answer