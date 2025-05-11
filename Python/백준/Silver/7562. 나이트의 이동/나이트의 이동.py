import sys
from collections import deque

T = int(input())
for _ in range(T):
    size = int(sys.stdin.readline())
    start_r, start_c = map(int, sys.stdin.readline().split())
    tar_r, tar_c = map(int, sys.stdin.readline().split())
    visited = list([0]*size for _ in range(size))
    dq = deque()
    dq.append([start_r,start_c])
    visited[start_r][start_c] = 1
    delta = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
    while dq:
        now_r, now_c = dq.popleft()
        if now_r == tar_r and now_c == tar_c:
            break
        for dr, dc in delta:
            new_r = now_r + dr
            new_c = now_c + dc
            if new_r >= size or new_r < 0 or new_c >= size or new_c < 0:
                continue
            if visited[new_r][new_c]:
                continue
            dq.append([new_r, new_c])
            visited[new_r][new_c] = visited[now_r][now_c] + 1

    sys.stdout.write(str(visited[tar_r][tar_c]-1)+'\n')

