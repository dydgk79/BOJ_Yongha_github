import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
ladders = dict()
snakes = dict()
visited = list([float('inf')]*10 for _ in range(10))

# 1번~100번 대신, 0번~99번 쓰기
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x-1] = y-1
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u-1] = v-1

q = list()
heappush(q, (0, 0))
visited[0][0] = 1
while visited[9][9] == float('inf'):
    now_count, now_block = heappop(q)
    for dice in range(1, 7):
        new_block = now_block + dice
        if new_block > 99:
            break
        new_ten = new_block // 10
        new_one = new_block % 10
        if visited[new_ten][new_one] <= now_count + 1:
            continue
        visited[new_ten][new_one] = now_count + 1
        if new_block in ladders.keys():
            ladder_block = ladders[new_block]
            if visited[ladder_block//10][ladder_block%10] <= now_count + 1:
                continue
            visited[ladder_block // 10][ladder_block % 10] = now_count + 1
            heappush(q, (now_count+1, ladder_block))
        elif new_block in snakes.keys():
            snake_block = snakes[new_block]
            if visited[snake_block // 10][snake_block % 10] <= now_count + 1:
                continue
            visited[snake_block // 10][snake_block % 10] = now_count + 1
            heappush(q, (now_count + 1, snake_block))
        else:
            heappush(q, (now_count+1, new_block))

print(visited[9][9])
