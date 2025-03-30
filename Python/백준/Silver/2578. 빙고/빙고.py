def check():
    global bingo_cnt
    global visited
    for r in range(5):
        for c in range(5):
            if chulsu_arr[r][c] == 0:
                if (r,0) not in visited and chulsu_arr[r][0] == chulsu_arr[r][1] == chulsu_arr[r][2] == chulsu_arr[r][3] == chulsu_arr[r][4] == 0:
                    bingo_cnt += 1
                    visited.add((r,0))
                    continue
                elif (0,c) not in visited and chulsu_arr[0][c] == chulsu_arr[1][c] == chulsu_arr[2][c] == chulsu_arr[3][c] == chulsu_arr[4][c] == 0:
                    bingo_cnt += 1
                    visited.add((0,c))
                    continue
                elif '00_to_44' not in visited and chulsu_arr[0][0] == chulsu_arr[1][1] == chulsu_arr[2][2] == chulsu_arr[3][3] == chulsu_arr[4][4] == 0:
                    bingo_cnt += 1
                    visited.add('00_to_44')
                    continue
                elif '04_to_40' not in visited and chulsu_arr[0][4] == chulsu_arr[1][3] == chulsu_arr[2][2] == chulsu_arr[3][1] == chulsu_arr[4][0] == 0:
                    bingo_cnt += 1
                    visited.add('04_to_40')


chulsu_arr = [list(map(int, input().split())) for _ in range(5)]
ans = 25
bingo_cnt = 0
visited = set()
ans_arr = [list(map(int, input().split())) for _ in range(5)]
ans_arr_1d = []
for row in ans_arr:
    ans_arr_1d.extend(row)
idx = 0
while bingo_cnt < 3:
    for r in range(5):
        for c in range(5):
            if chulsu_arr[r][c] == ans_arr_1d[idx]:
                chulsu_arr[r][c] = 0
                check()
                if bingo_cnt >= 3:
                    ans = min(ans, idx+1)
                    break
    idx += 1
print(ans)

