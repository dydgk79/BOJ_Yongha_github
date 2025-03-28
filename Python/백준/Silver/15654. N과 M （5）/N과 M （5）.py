def recur(n, now_list):
    if n == M:
        print(*now_list)
        return
    temp_list = now_list[:]
    for num in range(N):
        if arr[num] in temp_list:
            continue
        temp_list.append(arr[num])
        recur(n+1, temp_list)
        temp_list = now_list[:]


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
recur(0,[])
