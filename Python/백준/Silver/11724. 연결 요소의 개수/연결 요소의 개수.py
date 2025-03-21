import sys


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    if ref_x == ref_y:
        return
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
parents = [i for i in range(N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    union(s, e)

ancestor = set()
for idx in range(1, N+1):
    if find_set(idx) in ancestor:
        continue
    else:
        ancestor.add(find_set(idx))
print(len(ancestor))