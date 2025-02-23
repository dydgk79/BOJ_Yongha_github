T = int(input())

for _ in range(T):
    N = int(input())
    fibo_list = [[0,0] for _ in range(N+1)]
    fibo_list[0] = [1,0]
    if N > 0:
        fibo_list[1] = [0,1]
    idx = 2
    while idx <= N:
        fibo_list[idx][0] = fibo_list[idx-1][0] + fibo_list[idx-2][0]
        fibo_list[idx][1] = fibo_list[idx-1][1] + fibo_list[idx - 2][1]
        idx += 1
    print(*fibo_list[N])