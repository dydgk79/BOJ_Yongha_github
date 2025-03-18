def recur(cnt):
    if len(path) == M:
        print(*path)
        return
    if cnt == N:
        return
    for idx in range(1, N+1):
        if visited[idx]:
            continue
        visited[idx] = 1
        path.append(idx)
        recur(cnt+1)
        path.pop()
        visited[idx] = 0


N, M = map(int, input().split())
visited = [0]*(N+1)
path = []
recur(0)