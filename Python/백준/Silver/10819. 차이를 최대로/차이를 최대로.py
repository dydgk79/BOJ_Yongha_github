def calc_sum(nums):
    ans = 0
    temp_list = []
    for idx in range(N):
        temp_list.append(origin_arr[nums[idx]])
    index = 0
    while index < N-1:
        ans += abs(temp_list[index]-temp_list[index+1])
        index += 1
    return ans


def arr_make(length, now_arr):
    global ans
    if length == N:
        temp_sum = calc_sum(now_arr)
        if temp_sum > ans:
            ans = temp_sum
        return
    for idx in range(N):
        if idx in now_arr:
            continue
        arr_make(length+1, now_arr+[idx])


N = int(input())
ans = -float('inf')
origin_arr = list(map(int, input().split()))
arr_make(0, [])
print(ans)

