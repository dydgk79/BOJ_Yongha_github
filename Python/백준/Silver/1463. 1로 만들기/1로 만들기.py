N = int(input())

ans_list = [0]*(N+1)

idx = 2
while idx <= N:
    data3 = data2 = data1 = float('inf')
    if idx % 3 == 0:
        data3 = ans_list[idx//3] + 1
    if idx % 2 == 0:
        data2 = ans_list[idx//2] + 1
    data1 = ans_list[idx-1] + 1
    ans_list[idx] = min(data3, data2, data1)
    idx += 1
print(ans_list[N])