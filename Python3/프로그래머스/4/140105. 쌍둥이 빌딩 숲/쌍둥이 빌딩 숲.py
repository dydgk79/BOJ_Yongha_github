def solution(n, count):
    MOD = 1_000_000_007

    dp = [0] * (count + 1)
    dp[1] = 1

    for height in range(2, n + 1):
        new_dp = [0] * (count + 1)

        for visible in range(1, min(height, count) + 1):
            new_dp[visible] += dp[visible - 1]
            new_dp[visible] += dp[visible] * (2 * (height - 1))
            new_dp[visible] %= MOD

        dp = new_dp

    return dp[count]