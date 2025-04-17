def checker(length):
    num_set = set()
    if length == num_length:
        return num_length
    for idx in range(N):
        number = arr[idx][num_length-1:num_length-1-length:-1]
        if number in num_set:
            return checker(length+1)
        num_set.add(number)
    return length


import sys
N = int(sys.stdin.readline())
arr = [[] for _ in range(N)]
for idx in range(N):
    arr[idx] = sys.stdin.readline().strip()
num_length = len(arr[0])
print(checker(1))