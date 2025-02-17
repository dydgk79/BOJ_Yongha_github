input_arr = [list(map(int, input().split())) for _ in range(4)]

ans_arr = [[0]*100 for _ in range(100)]

for sqr in input_arr:
    for r in range(sqr[2]-sqr[0]):
        for c in range(sqr[3]-sqr[1]):
            ans_arr[sqr[0]+r][sqr[1]+c] += 1

cnt = 0
for r in range(100):
    for c in range(100):
        if ans_arr[r][c] != 0:
            cnt += 1
print(cnt)
