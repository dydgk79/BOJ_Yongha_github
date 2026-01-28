N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
movement = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

for _ in range(M):
    d, s = map(int, input().split())
    for idx in range(len(clouds)):
        clouds[idx][0] = (clouds[idx][0] + (movement[d][0] * s)) % N
        clouds[idx][1] = (clouds[idx][1] + (movement[d][1] * s)) % N
    added_bucket = set()
    for cloud in clouds:
        r, c = cloud
        arr[r][c] += 1
        added_bucket.add((r, c))

    for cloud in clouds:
        r, c = cloud
        count = 0
        for dr, dc in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N) or not (0 <= nc < N):
                continue
            if arr[nr][nc] > 0:
                count += 1
        arr[r][c] += count

    clouds = list()
    for r in range(N):
        for c in range(N):
            if ((r, c) not in added_bucket) and arr[r][c] >= 2:
                clouds.append([r, c])
                arr[r][c] -= 2

ans = 0
for row in arr:
    ans += sum(row)
print(ans)