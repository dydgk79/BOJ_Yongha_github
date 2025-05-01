from collections import deque


def mark_outside_air():
    dq = deque()
    dq.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while dq:
        r, c = dq.popleft()
        origin_arr[r][c] = -1
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if origin_arr[nr][nc] <= 0:
                    visited[nr][nc] = 1
                    dq.append((nr, nc))


def melt():
    melted = []
    for r, c in cheese_set:
        cnt = 0
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if origin_arr[nr][nc] == -1:
                cnt += 1
        if cnt >= 2:
            melted.append((r, c))
    for r, c in melted:
        origin_arr[r][c] = 0
        cheese_set.remove((r, c))


N, M = map(int, input().split())
origin_arr = [list(map(int, input().split())) for _ in range(N)]
cheese_set = {(r, c) for r in range(N) for c in range(M) if origin_arr[r][c] == 1}

time = 0
while cheese_set:
    mark_outside_air()
    melt()
    time += 1
print(time)
