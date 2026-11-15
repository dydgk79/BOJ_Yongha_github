T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    total = 0
    for idx in range(N - 1):
        total += abs(arr[idx] - arr[idx + 1])

    answer = total

    for idx in range(1, N - 1):
        a, b, c = arr[idx - 1], arr[idx], arr[idx + 1]

        dist = total - abs(a - b) - abs(b - c) + abs(a - c)
        answer = min(answer, dist)

    print(answer)