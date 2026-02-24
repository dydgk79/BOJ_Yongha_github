import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
S -= 1
G -= 1

visited = [-1]*F
q = deque()
q.append(S)
visited[S] = 0

while q:
    now = q.popleft()
    if now == G:
        break
    for delta in [U, -D]:
        nxt = now + delta
        if nxt >= F or nxt < 0:
            continue
        if visited[nxt] != -1:
            continue
        q.append(nxt)
        visited[nxt] = visited[now] + 1

if visited[G] != -1:
    print(visited[G])
else:
    print("use the stairs")