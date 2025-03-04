import sys

N, M = map(int, input().split())
input_arr = list(map(int, sys.stdin.readline().split()))
sum_list = [0]*N
idx = 0
ans = 0
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    while idx < j:
        ans += input_arr[idx]
        sum_list[idx] = ans
        idx += 1
    if i == 1:
        sys.stdout.write(str(sum_list[j-1]) + '\n')
    else:
        sys.stdout.write(str(sum_list[j-1]-sum_list[i-2]) + '\n')