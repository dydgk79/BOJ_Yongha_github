def recur(l, num):
    if l == M:
        print(*num)
        return
    for i in range(1, 1+N):
        for j in range(l):
            if i < num[j]:
                break
        else:
            temp_num = num
            temp_num[l] = i
            recur(l+1, temp_num)


N, M = map(int, input().split())
recur(0, [0]*M)
