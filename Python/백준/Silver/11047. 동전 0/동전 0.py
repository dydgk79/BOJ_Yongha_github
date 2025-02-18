N, K = map(int, input().split())
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))
ans = 0
for idx in range(N-1,-1,-1):
    if K >= coin_list[idx]:
       ans += K//coin_list[idx]
       K %= coin_list[idx]
print(ans)
