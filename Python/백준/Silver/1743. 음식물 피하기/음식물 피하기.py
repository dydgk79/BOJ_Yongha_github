from collections import deque


def bfs(r, c):
    global visited
    q = deque()
    q.append([r, c])
    temp_ans = 1
    while q:
        now_r, now_c = q.popleft()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            new_r = now_r + dr
            new_c = now_c + dc
            if (new_r, new_c) in visited:
                continue
            if not (0<=new_r<N and 0<=new_c<M):
                continue
            if arr[new_r][new_c] == 0:
                continue
            visited.add((new_r, new_c))
            q.append([new_r, new_c])
            temp_ans += 1
    return temp_ans


N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
visited = set()
max_ans = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        max_ans = max(max_ans, bfs(r, c))
print(max_ans)