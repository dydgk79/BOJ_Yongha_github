N = int(input())

arr = [(0, 0)] * N

for idx in range(N):
    x, y = map(int, input().split())
    arr[idx] = (x, y)

ans = 0
for idx in range(N):
    if idx == 0 or idx == 1:
        continue
    else:
        x1, y1 = arr[0]
        x2, y2 = arr[idx-1]
        x3, y3 = arr[idx]
        ans += (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
ans = abs(ans) * 0.5
print(f"{ans:.1f}")
