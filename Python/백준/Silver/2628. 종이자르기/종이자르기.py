C, R = map(int, input().split())
try_num = int(input())
R_arr = [0,R]
C_arr = [0,C]

for _ in range(try_num):
    a, cut = map(int, input().split())
    if a == 0:
        R_arr.append(cut)
    else:
        C_arr.append(cut)

R_arr.sort()
C_arr.sort()

max_R = 0
for idx in range(1, len(R_arr)):
    max_R = max(max_R, R_arr[idx]-R_arr[idx-1])

max_C = 0
for idx in range(1, len(C_arr)):
    max_C = max(max_C, C_arr[idx]-C_arr[idx-1])

print(max_R*max_C)