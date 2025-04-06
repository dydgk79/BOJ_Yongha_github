import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

ans = 0
for idx in range(N):
    tar = arr[idx]
    l = 0
    r = N-1
    while l<r:
        temp_sum = arr[l]+arr[r]
        if temp_sum == tar:
            if l != idx and r != idx:
                ans += 1
                break
            elif l == idx:
                l += 1
            else:
                r -= 1
        elif temp_sum < tar:
            l += 1
        else:
            r -= 1

print(ans)
