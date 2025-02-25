import sys

N = int(input())
M = int(input())

data = list([] for _ in range(N+1))

for _ in range(M):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

visited = [0]*(N+1)
q = list()
ans = 0

idx = 1
q.append(1)
visited[idx] = 1
while True:
    idx = q.pop(0)
    for item in data[idx]:
        if visited[item] == 0:
            visited[item] = 1
            q.append(item)
            ans += 1
    else:
        if q:
            continue
        else:
            break
print(ans)
