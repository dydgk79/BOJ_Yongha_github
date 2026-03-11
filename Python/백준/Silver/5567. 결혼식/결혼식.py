import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

arr = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr[a].append(b)
    arr[b].append(a)

q = deque()
visited = [0] * N
friends = set()
visited[0] = 1
q.append(0)

while q:
    now_friend = q.popleft()
    if visited[now_friend] > 2:
        continue
    next_friends = arr[now_friend]
    for next_friend in next_friends:
        if visited[next_friend] != 0:
            continue
        q.append(next_friend)
        visited[next_friend] = visited[now_friend] + 1
        friends.add(next_friend)
print(len(friends))
