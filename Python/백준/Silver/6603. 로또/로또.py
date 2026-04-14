import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    k = arr[0]
    arr_select = arr[1:len(arr)]
    for ans in combinations(arr_select, 6):
        print(*ans)
    print()