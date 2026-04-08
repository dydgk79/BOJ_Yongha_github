from collections import deque
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def checker(n):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    delta = [[0,1], [0,-1], [1,0], [-1,0]]
    region = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if arr[i][j] < n:
                continue
            q.append([i, j])
            visited[i][j] = region
            while q:
                now_r, now_c = q.popleft()
                for dr, dc in delta:
                    new_r = now_r + dr
                    new_c = now_c + dc
                    if not (0 <= new_r < N) or not (0 <= new_c < N):
                        continue
                    if visited[new_r][new_c]:
                        continue
                    if arr[new_r][new_c] < n:
                        continue
                    q.append([new_r, new_c])
                    visited[new_r][new_c] = region
            if visited[i][j] == region:
                region += 1
    return region - 1

ans = 0
for h in range(100):
    ans = max(ans, checker(h))
print(ans)