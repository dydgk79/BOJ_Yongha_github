import sys
sys.setrecursionlimit(10**7)
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = list([0]*n for _ in range(n))


def dfs(r, c):
    if dp[r][c] != 0:
        return dp[r][c]

    temp_step = 1

    for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
        new_r, new_c = r+dr, c+dc
        if 0 <= new_r < n and 0 <= new_c < n and arr[new_r][new_c] > arr[r][c]:
            temp_step = max(temp_step, dfs(new_r, new_c) + 1)

    dp[r][c] = temp_step
    return temp_step


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
