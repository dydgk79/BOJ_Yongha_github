T = int(input())

for tc in range(1, T + 1):
    N, P = map(int, input().split())

    dp = [1] * (N + 1)

    # 팩토리얼 메모이제이션
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] * i % P

    answer = 0

    # 아름다운 구간의 길이별 경우의 수
    for k in range(N):
        cnt = dp[N - k] * (N - k) * dp[k + 1]
        answer = (answer + cnt) % P

    print(f"#{tc} {answer}")