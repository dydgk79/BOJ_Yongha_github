import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
i = 0
j = N-1
cnt = 0
ans = 0
while i <= j:
    if cnt % 2 == 0:
        ans += arr[j]
        j -= 1
    else:
        ans -= arr[i]
        i += 1
    cnt += 1
if N%2 == 0:
    ans += arr[N//2 -1]
print(ans)