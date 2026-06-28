from collections import deque

T = int(input())
delta_8 = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def delta_search(x, y):
    count = 0
    for dx, dy in delta_8:
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < N) or not (0 <= new_y < N):
            continue
        if arr[new_x][new_y] == '*':
            count += 1
    return count

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    answer = 0
    zero_set = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.' and delta_search(i, j) == 0:
                zero_set.add((i, j))
    
    visited = [[False]*N for _ in range(N)]
    for zero_x, zero_y in zero_set:
        if visited[zero_x][zero_y]:
            continue
        answer += 1
        q = deque()
        q.append((zero_x, zero_y))
        visited[zero_x][zero_y] = True

        while q:
            now_x, now_y = q.popleft()
            if delta_search(now_x, now_y) != 0:
                continue
            for dx, dy in delta_8:
                new_x, new_y = now_x + dx, now_y + dy
                if not (0 <= new_x < N) or not (0 <= new_y < N):
                    continue
                if arr[new_x][new_y] == '*':
                    continue
                if visited[new_x][new_y]:
                    continue
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.' and not visited[i][j]:
                answer += 1

    print(f"#{test_case} {answer}")