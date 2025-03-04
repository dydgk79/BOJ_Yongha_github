n = int(input())
fibo_list = [0]*(n+1)
if n >= 1:
    fibo_list[1] = 1
if n >= 2:
    fibo_list[2] = 2
idx = 3
while idx <= n:
    fibo_list[idx] = fibo_list[idx-1] + fibo_list[idx-2]
    idx += 1
print(fibo_list[n]%10007)
