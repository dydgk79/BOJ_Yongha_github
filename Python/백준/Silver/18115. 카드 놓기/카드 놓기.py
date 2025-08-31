N = int(input())
A = list(map(int, input().split()))

origin_arr = [0]*N
now_num = N
start_idx = 0
temp_idx = 1
end_idx = N-1

for order in A:
    if order == 1:
        origin_arr[start_idx] = now_num
        start_idx += 1
        if start_idx < N and origin_arr[start_idx] != 0:
            start_idx = temp_idx
        temp_idx = start_idx + 1
    elif order == 2:
        origin_arr[temp_idx] = now_num
        temp_idx += 1
    else:
        origin_arr[end_idx] = now_num
        end_idx -= 1
    now_num -= 1

print(*origin_arr)
