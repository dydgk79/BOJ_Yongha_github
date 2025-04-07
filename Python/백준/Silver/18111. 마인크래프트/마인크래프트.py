def mining(height):
    global min_time
    global max_height
    global ans
    temp_time = 0
    temp_inv = B
    for idx in range(min_height, max_height+1):
        if idx == height:
            continue
        elif idx > height:
            temp_time += (idx-height)*2*counting_arr[idx]
            temp_inv += (idx-height)*counting_arr[idx]
        else:
            temp_time += (height-idx) * counting_arr[idx]
            temp_inv -= (height-idx) * counting_arr[idx]
    if temp_inv < 0:
        return
    if temp_time <= min_time:
        min_time = temp_time
        ans = height


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
counting_arr = [0]*257
for r in range(N):
    for c in range(M):
        counting_arr[arr[r][c]] += 1
min_time = float('inf')
max_height = 0
min_height = 256
for r in range(N):
    for c in range(M):
        max_height = max(max_height, arr[r][c])
        min_height = min(min_height, arr[r][c])

ans = 0
for idx in range(min_height, max_height+1):
    mining(idx)

print(min_time, ans)

