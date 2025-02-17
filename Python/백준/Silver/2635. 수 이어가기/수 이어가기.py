N = int(input())

ans_list = []
max_len = 0

for i in range(N):
    temp_list = [N]
    temp_n = N - i
    idx = 1
    while temp_n >= 0:
        temp_list.append(temp_n)
        temp_n = temp_list[idx-1] - temp_list[idx]
        idx += 1
    if max_len <= len(temp_list):
        max_len = len(temp_list)
        ans_list = temp_list

print(max_len)
for item in ans_list:
    print(item, end=" ")
print()