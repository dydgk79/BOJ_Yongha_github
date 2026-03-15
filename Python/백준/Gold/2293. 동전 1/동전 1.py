n, k = map(int, input().split())
arr = [-1]*n
for idx in range(n):
    arr[idx] = int(input())
arr.sort()

dp = [0]*(k+1)

dp[0] = 1

for coin in arr:
    for money in range(coin, k+1):
        dp[money] += dp[money-coin]

print(dp[-1])