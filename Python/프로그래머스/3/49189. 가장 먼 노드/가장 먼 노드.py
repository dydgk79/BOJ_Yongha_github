def solution(n, edge):
    from collections import deque
    answer = 0
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    visited = [0]*(n+1)
    q = deque()
    visited[1] = 1
    q.append(1)
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if visited[nxt]:
                continue
            q.append(nxt)
            visited[nxt] = visited[now] + 1
    max_num = max(visited)
    for num in visited:
        if num == max_num:
            answer += 1
    return answer