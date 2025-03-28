def recur(n, s, now_list):
    if n == M:
        print(*now_list)
        return
    temp_list = now_list[:]
    for num in range(s+1, N+1):
        temp_list.append(num)
        recur(n+1, num, temp_list)
        temp_list = now_list[:]


N, M = map(int, input().split())
recur(0,0,[])
