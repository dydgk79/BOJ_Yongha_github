import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
find_set = set()
for num in arr:
    find_set.add(num)

M = int(sys.stdin.readline())
finders = list(map(int, sys.stdin.readline().split()))
for finder in finders:
    if finder in find_set:
        print(1)
    else:
        print(0)
