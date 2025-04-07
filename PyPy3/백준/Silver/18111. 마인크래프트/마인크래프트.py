def mining(height):
    global min_time
    global max_height
    temp_time = 0
    temp_inv = B
    for r in range(N):
        for c in range(M):
            if arr[r][c] == height:
                continue
            elif arr[r][c] > height:
                temp_time += (arr[r][c]-height)*2
                temp_inv += arr[r][c]-height
            else:
                temp_time += height-arr[r][c]
                temp_inv -= height-arr[r][c]
    if temp_inv < 0:
        return
    if temp_time <= min_time:
        min_time = temp_time
        max_height = height


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
min_time = float('inf')
max_height = 0
min_height = 256
for r in range(N):
    for c in range(M):
        max_height = max(max_height, arr[r][c])
        min_height = min(min_height, arr[r][c])

for idx in range(min_height, max_height+1):
    mining(idx)

print(min_time, max_height)

