import sys

T = int(input())
for _ in range(T):
    N = int(input())
    input_data = [[]*N for _ in range(N)]
    for idx in range(N):
        input_data[idx] = list(map(int, sys.stdin.readline().split()))
    input_data.sort()
    ans = 1
    min_score = input_data[0][1]
    for idx in range(1,N):
        if input_data[idx][1] < min_score:
            ans += 1
            min_score = input_data[idx][1]
    print(ans)