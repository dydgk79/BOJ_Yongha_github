import sys

N = int(sys.stdin.readline())
arr = [0]*10001

for _ in range(N):
    new_num = int(sys.stdin.readline())
    arr[new_num] += 1

for idx in range(1,10001):
    while arr[idx]:
        sys.stdout.write(str(idx)+'\n')
        arr[idx] -= 1
