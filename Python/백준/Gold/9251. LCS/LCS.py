import sys
sentence_1 = sys.stdin.readline().strip()
sentence_2 = sys.stdin.readline().strip()

N = len(sentence_1)
M = len(sentence_2)

dp = [[0]*(M+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        if sentence_1[r-1] == sentence_2[c-1]:
            dp[r][c] = dp[r-1][c-1] + 1
        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])

print(dp[-1][-1])
