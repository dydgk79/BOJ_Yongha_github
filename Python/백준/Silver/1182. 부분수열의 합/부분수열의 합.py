def recur(level, total):
    global ans
    if level == N:
        if total == S:
            ans += 1
        return
    recur(level + 1, total + arr[level])
    recur(level + 1, total)


N, S = map(int, input().split())
arr = list(map(int, input().split()))

if S == 0:
    ans = -1
else:
    ans = 0
recur(0, 0)
print(ans)
