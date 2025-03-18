import sys

N = int(input())

arr = [0]*N
for idx in range(N):
    arr[idx] = int(sys.stdin.readline())
dp = [[0]*N for _ in range(2)]

if N == 1:
   print(arr[0])

else:
    dp[0][0] = dp[1][0] = arr[0]
    dp[0][1] = dp[0][0] + arr[1]
    dp[1][1] = arr[1]

    idx = 2
    while idx < N:
        dp[0][idx] = dp[1][idx-1] + arr[idx]
        dp[1][idx] = max(dp[0][idx-2], dp[1][idx-2]) + arr[idx]
        idx += 1

    max_value = max(dp[0][-1], dp[1][-1])
    print(max_value)
