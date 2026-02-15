import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

tails = []
for num in arr:
    x = -num
    l, r = 0, len(tails)
    while l < r:
        mid = (l + r) // 2
        if tails[mid] >= x:
            r = mid
        else:
            l = mid + 1
    if l == len(tails):
        tails.append(x)
    else:
        tails[l] = x

print(len(tails))