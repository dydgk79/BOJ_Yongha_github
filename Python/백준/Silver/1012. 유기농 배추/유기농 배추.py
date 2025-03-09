# T = int(input())
# num_data = [0]*11
# num_data[1] = 1
# num_data[2] = 2
# num_data[3] = 4
# for idx in range(4, 11):
#     num_data[idx] = num_data[idx-1] + num_data[idx-2] + num_data[idx-3]
#
# for _ in range(T):
#     n = int(input())
#     print(num_data[n])


def BFS(i,j):
    global visited
    global ans
    q = list()
    q.append([i,j])
    visited[i][j] = 1
    delta = [[1,0], [0,1], [-1,0], [0,-1]]
    while True:
        if q:
            now_i, now_j = q.pop(0)
            for d in delta:
                ni = now_i + d[0]
                nj = now_j + d[1]
                if 0<=ni<N and 0<=nj<M:
                    if visited[ni][nj] == 0 and plant_data[ni][nj] == 1:
                        q.append([ni,nj])
                        visited[ni][nj] = 1
        else:
            break


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    plant_data = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        plant_data[r][c] = 1
    visited = [[0]*M for _ in range(N)]
    ans = 0
    for i_idx in range(N):
        for j_idx in range(M):
            if visited[i_idx][j_idx] == 0 and plant_data[i_idx][j_idx]:
                ans += 1
                BFS(i_idx, j_idx)
    print(ans)
