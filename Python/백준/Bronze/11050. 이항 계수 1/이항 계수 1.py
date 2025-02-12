N, K = map(int, input().split())

ans = 1
for i in range(1, K+1):
    ans *= (N+1-i)
    ans //= i
print(ans)