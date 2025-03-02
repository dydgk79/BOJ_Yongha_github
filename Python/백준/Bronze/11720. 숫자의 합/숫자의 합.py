N = int(input())
input_list = list(map(int,input()))
sum = 0
for idx in range(N):
    sum += input_list[idx]
print(sum)