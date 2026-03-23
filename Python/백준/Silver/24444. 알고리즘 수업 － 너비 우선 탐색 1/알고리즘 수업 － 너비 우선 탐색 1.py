import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M, R = map(int, input().split())

arr = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0]*(N+1)
step = 1
visited[R] = step
q = deque()
q.append(R)
while q:
    now = q.popleft()
    arr[now].sort()
    for nxt in arr[now]:
        if visited[nxt]:
            continue
        step += 1
        visited[nxt] = step
        q.append(nxt)

for idx in range(1, N+1):
    print(str(visited[idx])+"\n")