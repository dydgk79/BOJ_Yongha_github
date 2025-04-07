import sys
from collections import deque


def bfs(idx):
    global visited_arr
    q = deque()
    for f in friend[idx]:
        visited_arr[idx][f] = 1
        q.append(f)
    while q:
        now_friend = q.popleft()
        for new_f in friend[now_friend]:
            if new_f == idx:
                continue
            f_cnt = visited_arr[idx][now_friend] + 1
            if f_cnt < visited_arr[idx][new_f]:
                visited_arr[idx][new_f] = f_cnt
                q.append(new_f)


N, M = map(int, input().split())
friend = [[] for _ in range(N+1)]
visited_arr = [[float('inf')]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)
for r in range(N+1):
    for c in range(N+1):
        if r == c or r == 0 or c == 0:
            visited_arr[r][c] = 0
for idx in range(0, N+1):
    bfs(idx)

min_sum = float('inf')
ans_idx = 0
for idx in range(1, N+1):
    temp_sum = sum(visited_arr[idx])
    if temp_sum < min_sum:
        min_sum = temp_sum
        ans_idx = idx
print(ans_idx)

