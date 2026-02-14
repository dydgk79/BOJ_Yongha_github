import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list()
for idx in range(N):
    arr.append(list(map(int, input().split())))

dp = [0]*(N+1)
for idx in range(N-1, -1, -1):
    t, p = arr[idx]
    if idx + t <= N:
        dp[idx] = max(dp[idx+1], p + dp[idx + t])
    else:
        dp[idx] = dp[idx+1]

print(dp[0])
