def solution(money):
    def rob(arr):
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(dp[0], arr[1])

        for idx in range(2, len(arr)):
            dp[idx] = max(dp[idx-2] + arr[idx], dp[idx-1])

        return dp[-1]

    answer = max(rob(money[:-1]), rob(money[1:]))
    return answer