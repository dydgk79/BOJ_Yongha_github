import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1]*n for _ in range(n)]  # 각 칸에 도착하는 최장 길이 (최소 1)

cells = []
for r in range(n):
    for c in range(n):
        cells.append((arr[r][c], r, c))

cells.sort()  # 값 오름차순

dirs = [(1,0),(0,1),(-1,0),(0,-1)]

ans = 1
for val, r, c in cells:
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] > val:
            # (r,c)에서 (nr,nc)로 이동 가능: 더 큰 값으로 전이
            if dp[nr][nc] < dp[r][c] + 1:
                dp[nr][nc] = dp[r][c] + 1
                if ans < dp[nr][nc]:
                    ans = dp[nr][nc]

print(ans)