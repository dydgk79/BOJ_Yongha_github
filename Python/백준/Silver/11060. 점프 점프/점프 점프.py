N = int(input())
arr = list(map(int, input().split()))
dp = [float('inf')]*N
dp[0] = 0
idx = 0
while dp[-1] == float('inf'):
    jump_num = arr[idx]
    for num in range(jump_num, 0, -1):
        if num + idx >= N:
            continue
        jump_cnt = dp[idx] + 1
        if dp[num + idx] < jump_cnt:
            continue
        else:
            dp[num+idx] = jump_cnt
    idx += 1
    if idx == N:
        dp[-1] = -1

print(dp[-1])