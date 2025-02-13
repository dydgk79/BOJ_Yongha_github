N, B = map(int, input().split())

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ans = []

remain = 0
while N//B > 0:
    remain = N % B
    if 0 <= remain <= 9:
        ans.append(str(remain))
    else:
        ans.append(alpha[remain - 10])
    N //= B
if 0 <= N <= 9:
    ans.append(str(N))
else:
    ans.append(alpha[N - 10])

ans = reversed(ans)
print(''.join(ans))
