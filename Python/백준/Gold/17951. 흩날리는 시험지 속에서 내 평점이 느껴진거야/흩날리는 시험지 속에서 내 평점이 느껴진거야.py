import sys

N, K = map(int, sys.stdin.readline().rstrip('\n').split())
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))

lt, rt = 0, sum(arr)
ans = 0

def can_make(x):
    cnt = 0
    s = 0
    for v in arr:
        s += v
        if s >= x:
            cnt += 1
            s = 0
    return cnt >= K

while lt <= rt:
    mid = (lt + rt) // 2
    if can_make(mid):
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)