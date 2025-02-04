N, M = map(int, input().split())
num = list(map(int, input().split()))
sum = 0
for idx_1 in range(len(num)):
    for idx_2 in range(len(num)):
        for idx_3 in range(len(num)):
            try:
                if idx_1 < idx_2 < idx_3:
                    temp = num[idx_1] + num[idx_2] + num[idx_3]
                    if temp <= M:
                        if sum < temp:
                            sum = temp
            except IndexError:
                continue

print(sum)

