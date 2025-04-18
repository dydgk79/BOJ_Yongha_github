N = int(input())

ans_list = [0]*(N+1)
zero_list = [0]*(N+1)
num_list = [0]*(N+1)

ans_list[1] = 3
zero_list[1] = 1
num_list[1] = 1

idx = 2
while idx <= N:
    zero_list[idx] = ans_list[idx-1]%9901
    num_list[idx] = (zero_list[idx-1]+num_list[idx-1])%9901
    ans_list[idx] = (zero_list[idx]+2*num_list[idx])%9901
    idx += 1
print(ans_list[N] % 9901)