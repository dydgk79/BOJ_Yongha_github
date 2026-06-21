TC = int(input())

for _ in range(TC):
    N = int(input())
    arr = [[]*N for _ in range(N)]
    for idx in range(N):
        D, T = map(int, input().split())
        arr[idx] = [D, T]
    arr.sort(key=lambda x: x[1])
    ans = arr[N-1][1] - arr[N-1][0]
    for idx_rev in range(N-2, -1, -1):
        now_D, now_T = arr[idx_rev]
        if now_T > ans:
            ans -= now_D
        else:
            ans = now_T - now_D
    print(ans)