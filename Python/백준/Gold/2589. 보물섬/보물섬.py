from collections import deque

height, width = map(int, input().split())
map_data = list(input() for _ in range(height))

enable_point = deque()

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for r in range(height):
    for c in range(width):
        if map_data[r][c] == 'W':
            continue
        current_enable_root = 0
        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            if not (0 <= new_r < height) or not (0 <= new_c < width):
                continue
            if map_data[new_r][new_c] == 'W':
                continue
            current_enable_root += 1
        if current_enable_root == 1 or current_enable_root == 2:
            enable_point.append([r, c])

ans = 0
for enable_r, enable_c in enable_point:
    q = deque()
    visited = list([0] * width for _ in range(height))
    q.append([enable_r, enable_c])
    visited[enable_r][enable_c] = 1
    while q:
        now_r, now_c = q.popleft()
        for dr, dc in directions:
            new_r = now_r + dr
            new_c = now_c + dc
            if not (0 <= new_r < height) or not (0 <= new_c < width):
                continue
            if map_data[new_r][new_c] == 'W':
                continue
            if visited[new_r][new_c]:
                continue
            visited[new_r][new_c] = visited[now_r][now_c] + 1
            q.append([new_r, new_c])
    ans = max(ans, max(map(max, visited)) - 1)

print(ans)
