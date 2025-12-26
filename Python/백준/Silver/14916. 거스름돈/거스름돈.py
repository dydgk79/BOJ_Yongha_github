n = int(input())
ans = 0

# 2와 5의 공배수는 무조건 최소갯수가 정해져있으니까 먼저 하고, 나머지를 예외처리
ans += 2*(n//10)
n %= 10

if n == 0:
    print(ans)
elif n == 1:
    if ans >= 1:
        # 5원짜리 하나를 2원짜리 3개로 대체
        print(ans + 2)
    else:
        print(-1)
elif n == 2:
    print(ans + 1)
elif n == 3:
    if ans >= 1:
        print(ans + 3)
    else:
        print(-1)
elif n == 4:
    print(ans + 2)
elif n == 5:
    print(ans + 1)
elif n == 6:
    print(ans + 3)
elif n == 7:
    print(ans + 2)
elif n == 8:
    print(ans + 4)
elif n == 9:
    print(ans + 3)
