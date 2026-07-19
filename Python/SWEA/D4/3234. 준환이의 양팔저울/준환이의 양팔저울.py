import math

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_sum = sum(arr)
    answer = 0
    visited = [False] * N

    def checker(n, left_sum, right_sum):
        global answer

        if left_sum >= arr_sum - left_sum:
            remain = N - n
            answer += math.factorial(remain) * (2 ** remain)
            return

        if n == N:
            answer += 1
            return

        for i in range(N):
            if visited[i]:
                continue

            visited[i] = True

            checker(n + 1, left_sum + arr[i], right_sum)

            if left_sum >= right_sum + arr[i]:
                checker(n + 1, left_sum, right_sum + arr[i])

            visited[i] = False

    checker(0, 0, 0)

    print(f"#{test_case} {answer}")