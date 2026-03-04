N = int(input())
arr = list(map(int, input().split()))
M = int(input())

l, r = 0, max(arr)
mid = 0
ans = 0

if sum(arr) <= M:
    ans = max(arr)
else:
    while l <= r:
        mid = (l + r) // 2
        asset = M
        for idx in range(len(arr)):
            if arr[idx] > mid:
                asset -= mid
            else:
                asset -= arr[idx]
        if asset < 0:
            r = mid - 1
        elif asset >= 0:
            l = mid + 1
            ans = max(ans, mid)

print(ans)