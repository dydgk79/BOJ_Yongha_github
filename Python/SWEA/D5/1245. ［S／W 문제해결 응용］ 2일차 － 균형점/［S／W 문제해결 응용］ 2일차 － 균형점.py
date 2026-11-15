
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    positions = arr[:N]
    masses = arr[N:]

    answer = []

    for idx in range(N - 1):
        left = positions[idx]
        right = positions[idx + 1]

        for _ in range(100):
            mid = (left + right) / 2
            force = 0

            for j in range(N):
                F = masses[j] / (mid - positions[j]) ** 2

                if positions[j] < mid:
                    force -= F
                else:
                    force += F

            if force < 0:
                left = mid
            else:
                right = mid

        answer.append((left + right) / 2)

    print(f"#{tc}", *[f"{x:.10f}" for x in answer])
