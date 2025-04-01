from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    counting_arr = deque()
    for idx in range(N):
        counting_arr.append([arr[idx], idx])
    max_num = max(counting_arr)
    while counting_arr:
        data = counting_arr.popleft()
        if data[0] == max_num[0]:
            cnt += 1
            if data[1] == M:
                print(cnt)
                break
            else:
                max_num = max(counting_arr)
        else:
            counting_arr.append(data)
