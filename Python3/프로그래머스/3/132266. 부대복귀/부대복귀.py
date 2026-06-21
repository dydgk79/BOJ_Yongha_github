def solution(n, roads, sources, destination):
    from collections import deque
    answer = [-1]*len(sources)
    arr = [[] for _ in range(n+1)]
    for road in roads:
        arr[road[0]].append(road[1])
        arr[road[1]].append(road[0])
    q = deque()
    q.append(destination)
    visited = [-1]*(n+1)
    visited[destination] = 0
    finder = set()
    for source in sources:
        finder.add(source)
    while q and finder:
        now = q.popleft()
        for next_target in arr[now]:
            if visited[next_target] >= 0:
                continue
            q.append(next_target)
            visited[next_target] = visited[now] + 1
            if next_target in finder:
                finder.remove(next_target)
    
    for idx in range(len(sources)):
        answer[idx] = visited[sources[idx]]
            
    return answer