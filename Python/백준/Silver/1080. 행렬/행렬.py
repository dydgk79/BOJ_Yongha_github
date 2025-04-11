import sys

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
tar_arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

ans = 0
if N >= 3 and M >= 3:
    r = c = 0
    while ans >= 0:
        if arr[r][c] != tar_arr[r][c]:
            for dr in range(r, r+3):
                for dc in range(c, c+3):
                    arr[dr][dc] = (arr[dr][dc]+1) % 2
            ans += 1
        c += 1
        if c == M-2:
            c = 0
            r += 1
            if r == N-2:
                break

for r in range(N):
    if ans == -1:
        break
    for c in range(M):
        if arr[r][c] != tar_arr[r][c]:
            ans = -1
            break

print(ans)
