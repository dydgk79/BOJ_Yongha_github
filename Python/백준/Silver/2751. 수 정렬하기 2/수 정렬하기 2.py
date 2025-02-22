import sys
N = int(sys.stdin.readline())

ans = [0]*N
for idx in range(N):
    ans[idx] = int(sys.stdin.readline())
ans.sort()
for i in ans:
    i = str(i)
    sys.stdout.write(i + '\n')