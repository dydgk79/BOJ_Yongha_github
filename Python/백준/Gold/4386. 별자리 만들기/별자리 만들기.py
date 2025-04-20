import sys
from heapq import heappush, heappop
import math


def calc_distance(x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2
    return round(math.sqrt(dx**2 + dy**2), 2)


def prim():
    hq = []
    dist_count = [float('inf') for _ in range(n)]
    heappush(hq, [0,star_list[0]])
    dist_count[0] = 0
    ans = 0
    cnt = 0
    visited = set()
    while hq:
        if len(visited) == n:
            break
        cost, [now_x, now_y] = heappop(hq)
        if (now_x, now_y) in visited:
            continue
        visited.add((now_x, now_y))
        ans += cost
        cnt += 1
        for idx in range(n):
            new_x, new_y = star_list[idx]
            if (new_x, new_y) in visited:
                continue
            dist = calc_distance(now_x, now_y, new_x, new_y)
            if dist >= dist_count[idx]:
                continue
            dist_count[idx] = dist
            heappush(hq, [dist, star_list[idx]])

    return round(ans, 2)


n = int(sys.stdin.readline())

star_list = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    star_list.append([x,y])
print(f'{prim():0.2f}')