N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
arr = set(arr)
arr = list(arr)
arr.sort()
length = len(arr)
max_len = -float('inf')
for idx in range(length):
    if len(arr[idx]) > max_len:
        max_len = len(arr[idx])


for leng in range(1,max_len+1):
    for idx in range(length):
        if len(arr[idx]) == leng:
            print(arr[idx])

