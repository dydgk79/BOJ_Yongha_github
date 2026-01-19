# 나무위키 코드 참고
def eratosthenes(num: int = 1000000):
    MAX = num + 1
    LIM = int(num ** 0.5) + 1
    RSET = lambda strt, end, gap: set(range(strt, end, gap))

    prime = RSET(5, MAX, 6) | RSET(7, MAX, 6)
    if num > 2: prime.add(3)
    if num > 1: prime.add(2)
    for i in range(5, LIM, 6):
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)

    return prime

prime_set = eratosthenes(1000000)

T = int(input())

for _ in range(T):
    N = int(input())
    count = 0
    for a in range(2, N//2 + 1):
        b = N - a
        if a in prime_set and b in prime_set:
            count += 1
    print(count)
