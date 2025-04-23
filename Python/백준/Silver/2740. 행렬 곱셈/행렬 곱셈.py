N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

ans = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        temp = 0
        for k in range(M):
            temp += A[i][k] * B[k][j]
        ans[i][j] = temp

for row in ans:
    print(*row)