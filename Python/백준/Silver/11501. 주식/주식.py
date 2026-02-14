import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    temp_max = 0
    ans = 0
    for idx in range(N-1, -1, -1):
        if arr[idx] > temp_max:
            temp_max = arr[idx]
        else:
            ans += temp_max - arr[idx]
    print(ans)