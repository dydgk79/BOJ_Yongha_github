from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_cnt = 0
dq = deque()
visited = [[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            dq.append([r,c])
            visited[r][c] = 1
            arr_cnt += 1
        elif arr[r][c] == -1:
            visited[r][c] = 1
            arr_cnt += 1

while dq:
    now_r, now_c = dq.popleft()
    for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
        new_r = now_r + dr
        new_c = now_c + dc
        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
            continue
        if arr[new_r][new_c] == -1 and visited[new_r][new_c] == 0:
            arr_cnt += 1
            visited[new_r][new_c] = 1
            continue
        if visited[new_r][new_c] >= 1:
            continue
        else:
            if visited[new_r][new_c] == 0:
                visited[new_r][new_c] = visited[now_r][now_c] + 1
                arr_cnt += 1
                dq.append([new_r,new_c])
ans = 0
for row in visited:
    if 0 in row:
        ans = 0
        break
    ans = max(max(row), ans)
print(ans-1)
