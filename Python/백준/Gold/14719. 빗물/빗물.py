H, W = map(int, input().split())
arr = list(map(int, input().split()))

left_max = [0] * W
right_max = [0] * W
left_max[0] = arr[0]
right_max[W-1] = arr[W-1]

for idx in range(1, W):
    left_max[idx] = max(left_max[idx-1], arr[idx])
    right_max[W-idx-1] = max(right_max[W-idx], arr[W-idx-1])

ans = 0
for idx in range(W):
    ans += min(left_max[idx], right_max[idx]) - arr[idx]

print(ans)