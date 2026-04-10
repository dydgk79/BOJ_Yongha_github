import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
truth = list(map(int, input().split()))
visited = [0] * (N+1)

# 진실을 알면 visited가 1
for idx in range(1, len(truth)):
    visited[truth[idx]] = 1

# 몇번 파티에 누구누구가 참가했는지 기록
party = [list() for _ in range(M+1)]
# 누가 몇번 파티에 참가했는지 기록
joined = [list() for _ in range(N+1)]

for idx in range(M):
    new_party = list(map(int, input().split()))
    for idx_2 in range(1, len(new_party)):
        party[idx+1].append(new_party[idx_2])
        joined[new_party[idx_2]].append(idx + 1)

truth_party = set()
q = deque()
for idx in range(1,len(truth)):
    q.append(truth[idx])
while q:
    now = q.popleft()
    for next_party in joined[now]:
        truth_party.add(next_party)
        for next_people in party[next_party]:
            if visited[next_people]:
                continue
            q.append(next_people)
            visited[next_people] = 1
            
print(M-len(truth_party))