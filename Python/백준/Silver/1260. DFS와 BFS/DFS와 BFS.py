import sys
from collections import deque


def DFS(n):
    visited_DFS[n] = 1
    print(n, end=" ")
    for data in graph[n]:
        if visited_DFS[data] == 0:
            DFS(data)


def BFS(n):
    dq = deque()
    dq.append(n)
    visited = [0]*(N+1)
    visited[n] = 1
    while dq:
        now_n = dq.popleft()
        print(now_n, end=" ")
        for data in graph[now_n]:
            if visited[data]:
                continue
            dq.append(data)
            visited[data] = 1


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for idx in range(N+1):
    graph[idx].sort()

visited_DFS = [0]*(N+1)
DFS(V)

print()

BFS(V)
