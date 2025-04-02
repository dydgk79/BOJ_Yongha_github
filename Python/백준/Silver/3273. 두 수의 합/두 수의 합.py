n = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()

cnt = 0

si = 0
ei = n-1

while si < ei:
    temp_sum = arr[si] + arr[ei]
    if temp_sum == target:
        cnt += 1
        si += 1
        ei -= 1
    elif temp_sum > target:
        ei -= 1
    else:
        si += 1
print(cnt)
