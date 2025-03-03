N, M = map(int, input().split())

arr_data = list([]*M for _ in range(N))

for idx in range(N):
    arr_data[idx] = list(map(int,input()))

delta = [[0,1], [1,0], [0,-1], [-1,0]]

q = list()
visited = [[0]*M for _ in range(N)]

for idx in range(M):
    if arr_data[0][idx] == 0:
        q.append([0,idx])
        visited[0][idx] = 1

i = j = 0
ans = False

while q:
    i, j = q.pop(0)
    if i == N-1:
        ans = True
        break
    for d in delta:
        ni = i+d[0]
        nj = j+d[1]
        if 0<=ni<N and 0<=nj<M:
            if arr_data[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append([ni,nj])
                visited[ni][nj] = 1
    if q:
        continue
    else:
        ans = False
        break

if ans:
    print('YES')
else:
    print('NO')