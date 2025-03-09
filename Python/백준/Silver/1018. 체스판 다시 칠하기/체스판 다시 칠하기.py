def board_checker(color, i, j):
    cnt = 0
    for r in range(i, i+8):
        for c in range(j, j+8):
            if (r+c-i-j)%2 == 0:
                target_color = color
            else:
                if color == 'W':
                    target_color = 'B'
                else:
                    target_color = 'W'
            if board_data[r][c] != target_color:
                cnt += 1
    return cnt


def board_checker_32(color, i, j):
    rcnt = 0
    if color == 'W':
        new_color = 'B'
    else:
        new_color = 'W'
    for r in range(i, i+8):
        for c in range(j, j+8):
            if (r+c-i-j)%2 == 0:
                target_color = new_color
            else:
                if new_color == 'W':
                    target_color = 'B'
                else:
                    target_color = 'W'
            if board_data[r][c] != target_color:
                rcnt += 1
    return rcnt


N, M = map(int, input().split())
board_data = [input() for _ in range(N)]
min_paint = float('inf')
for row in range(N-7):
    for col in range(M-7):
        paint_cnt = board_checker(board_data[row][col], row, col)
        reverse_paint_color = board_checker_32(board_data[row][col], row, col)
        min_paint = min(paint_cnt, reverse_paint_color, min_paint)
print(min_paint)
