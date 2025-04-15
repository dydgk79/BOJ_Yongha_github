from heapq import heappop, heappush
import sys

N = int(sys.stdin.readline())
hq = []

for _ in range(N):
    order = int(sys.stdin.readline())
    if order == 0:
        if len(hq) == 0:
            sys.stdout.write('0\n')
        else:
            print(-heappop(hq))
    else:
        heappush(hq, -order)