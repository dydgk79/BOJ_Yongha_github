import sys
from collections import deque


def bfs_tar1(n):
    dq = deque()
    visited = set()
    dq.append(n)
    visited.add(n)
    while dq:
        now = dq.popleft()
        for parent in par[now]:
            if parent in visited:
                continue
            dq.append(parent)
            visited.add(parent)
    return visited


def bfs_tar2(n):
    dq = deque()
    visited = set()
    dq.append(n)
    visited.add(n)
    final = n
    while dq:
        now = dq.popleft()
        if now in tar1_pars:
            return now
        for parent in par[now]:
            if parent in visited:
                continue
            dq.append(parent)
            visited.add(parent)
        final = now
    return final


T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    par = [[] for _ in range(N+1)]
    for _ in range(N-1):
        p, c = map(int,sys.stdin.readline().split())
        par[c].append(p)
    tar1, tar2 = map(int,sys.stdin.readline().split())
    tar1_pars = bfs_tar1(tar1)
    print(bfs_tar2(tar2))


