def cook(level, S, B, start, flag):
    global min_taste_dif

    if level == N:
        if flag == 0:
            return
        taste_dif = abs(S-B)
        min_taste_dif = min(min_taste_dif, taste_dif)
        return
    for idx in range(start,N):
        cook(level + 1, S * arr[idx][0], B + arr[idx][1], idx + 1, flag+1)
        cook(level+1, S, B, idx+1, flag)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

min_taste_dif = float('inf')

cook(0, 1, 0, 0, 0)
print(min_taste_dif)