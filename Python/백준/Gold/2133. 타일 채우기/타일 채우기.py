N = int(input())

arr = [0]*31
arr[2] = 3
arr[4] = 11

for idx in range(6, 31, 2):
    arr[idx] = (arr[idx-2] * 4) - (arr[idx-4])

print(arr[N])