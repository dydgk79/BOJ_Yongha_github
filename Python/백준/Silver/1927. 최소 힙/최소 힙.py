import sys
from heapq import heappush, heappop

N = int(input())

heap = []
for _ in range(N):
    order = int(sys.stdin.readline())
    if order:
        heappush(heap, order)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)