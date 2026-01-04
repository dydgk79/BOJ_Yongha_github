# LCA
import sys
from collections import deque

N = int(sys.stdin.readline())

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

parent = [0 for _ in range(N + 1)]
depth = [0 for _ in range(N + 1)]
queue = deque([1])
while queue:
    now = queue.popleft()
    for i in adj[now]:
        if i == 1 or parent[i]:
            continue
        queue.append(i)
        parent[i] = now
        depth[i] = depth[now] + 1

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if depth[a] > depth[b]:
        while depth[a] != depth[b]:
            a = parent[a]
    elif depth[a] < depth[b]:
        while depth[a] != depth[b]:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)