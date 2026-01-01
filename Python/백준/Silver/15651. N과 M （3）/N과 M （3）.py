N, M = map(int, input().split())


def dfs(s):
    global arr
    if s == M:
        print(*arr)
        return
    for i in range(1, N+1):
        arr.append(i)
        dfs(s+1)
        arr.pop()


arr = []

dfs(0)