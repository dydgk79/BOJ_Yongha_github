def facto(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*facto(n-1)


N = int(input())

cnt = 0
ans = str(facto(N))
for idx in range(len(ans)-1,-1,-1):
    if ans[idx] == '0':
        cnt += 1
    else: break
print(cnt)