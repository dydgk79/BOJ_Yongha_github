from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]

    # 직사각형 전체 영역을 1로 채움
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    # 직사각형 내부를 0으로 지워 테두리만 남김
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    start_x = characterX * 2
    start_y = characterY * 2
    target_x = itemX * 2
    target_y = itemY * 2

    visited = [[-1] * 102 for _ in range(102)]
    visited[start_x][start_y] = 0

    queue = deque([(start_x, start_y)])

    delta = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while queue:
        x, y = queue.popleft()

        if x == target_x and y == target_y:
            return visited[x][y] // 2

        for dx, dy in delta:
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < 102 and 0 <= new_y < 102):
                continue

            if board[new_x][new_y] == 0:
                continue

            if visited[new_x][new_y] != -1:
                continue

            visited[new_x][new_y] = visited[x][y] + 1
            queue.append((new_x, new_y))