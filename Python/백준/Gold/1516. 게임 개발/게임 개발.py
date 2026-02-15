import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp[i] : i번(0-index) 건물의 최소 완료 시간
dp = [0] * N

# 위상정렬 준비
graph = [[] for _ in range(N)]   # 선행 -> 후행
indegree = [0] * N

# arr[i] = [time, pre1, pre2, ..., -1]
for i in range(N):
    time = arr[i][0]
    prereqs = arr[i][1:-1]
    indegree[i] = len(prereqs)
    for p in prereqs:
        graph[p - 1].append(i)

# indegree 0부터 시작
q = deque()
for i in range(N):
    if indegree[i] == 0:
        dp[i] = arr[i][0]   # 선행 없으면 자기 시간부터 시작
        q.append(i)

# 위상정렬 + DP
while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        # nxt는 cur가 끝나야 시작 가능하므로, dp[nxt] 후보 갱신
        dp[nxt] = max(dp[nxt], dp[cur] + arr[nxt][0])

        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

# 출력
for t in dp:
    sys.stdout.write(str(t) + '\n')
