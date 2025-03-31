n=int(input())
a = list(map(int,input().split()))
c=set()
cnt = 0
for idx in range(n):
    if a[idx] in c:
        cnt += 1
    c.add(a[idx])

print(cnt)
