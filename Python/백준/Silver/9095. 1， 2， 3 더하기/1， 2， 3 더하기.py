T = int(input())
num_data = [0]*11
num_data[1] = 1
num_data[2] = 2
num_data[3] = 4
for idx in range(4, 11):
    num_data[idx] = num_data[idx-1] + num_data[idx-2] + num_data[idx-3]

for _ in range(T):
    n = int(input())
    print(num_data[n])