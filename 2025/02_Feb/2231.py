N = int(input())
for idx in range(1, N+1):
    num = idx
    sum = idx
    while num // 10 >= 1:
        sum += num%10
        num //= 10
    sum += num
    if sum == N:
        print(idx)
        break
    elif idx == N:
        print(0)