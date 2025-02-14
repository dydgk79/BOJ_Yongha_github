N = int(input())
ans = []

for idx in range(N):
    x, y = map(int,input().split())
    ans.append((x,y))

ans.sort()
for idx in range(N):
    print(*ans[idx])