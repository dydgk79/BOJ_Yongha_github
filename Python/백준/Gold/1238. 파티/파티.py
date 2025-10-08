from heapq import heappush, heappop


def bfs():
    q = list()
    q.append([0, X])
    visited = set()
    while q:
        now_dist, now_vil = heappop(q)
        if now_vil in visited:
            continue
        go_count[now_vil] = now_dist
        visited.add(now_vil)
        for search_idx in range(1, N+1):
            if search_idx in visited:
                continue
            if arr[now_vil][search_idx] == -1:
                continue
            if now_dist+arr[now_vil][search_idx] > go_count[search_idx]:
                continue
            heappush(q, [now_dist+arr[now_vil][search_idx], search_idx])
    q = list()
    q.append([0, X])
    visited = set()
    while q:
        now_dist, now_vil = heappop(q)
        if now_vil in visited:
            continue
        back_count[now_vil] = now_dist
        visited.add(now_vil)
        for search_idx in range(1, N + 1):
            if search_idx in visited:
                continue
            if arr_reverse[now_vil][search_idx] == -1:
                continue
            if now_dist+arr_reverse[now_vil][search_idx] > back_count[search_idx]:
                continue
            heappush(q, [now_dist + arr_reverse[now_vil][search_idx], search_idx])


N, M, X = map(int, input().split())
arr = [[-1]*(N+1) for _ in range(N+1)]
arr_reverse = [[-1]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    arr[s][e] = t
    arr_reverse[e][s] = t

ans = 0
go_count = [float('inf')]*(N+1)
back_count = [float('inf')]*(N+1)

bfs()

for idx in range(1, N+1):
    ans = max(ans, go_count[idx]+back_count[idx])

print(ans)
