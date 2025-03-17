paper = [[0]*100 for _ in range(100)]
cnt = 0

for _ in range(4):
    arr = list(map(int, input().split()))

    for i in range(arr[0], arr[2]):
        for j in range(arr[1], arr[3]):
            paper[i][j] += 1

for i in range(100):
    for j in range(100):
        if paper[i][j] >= 1:
            cnt += 1

print(cnt)
