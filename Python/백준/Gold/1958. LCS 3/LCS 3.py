first_input = list(input())
second_input = list(input())
third_input = list(input())

len_first = len(first_input)
len_second = len(second_input)
len_third = len(third_input)

dp = [[[0] * (len_third + 1) for _ in range(len_second + 1)] for _ in range(len_first + 1)]

for i in range(len_first):
    for j in range(len_second):
        for k in range(len_third):
            if first_input[i] == second_input[j] == third_input[k]:
                dp[i+1][j+1][k+1] = dp[i][j][k] + 1
            else:
                dp[i+1][j+1][k+1] = max(dp[i][j+1][k+1], dp[i+1][j][k+1], dp[i+1][j+1][k], dp[i][j][k])

print(dp[len_first][len_second][len_third])