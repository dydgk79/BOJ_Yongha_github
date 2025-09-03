ISBN = input()

sum = 0
damaged_idx = -1
for idx in range(12):
    if ISBN[idx] == '*':
        damaged_idx = idx
    else:
        if idx%2 == 0:
            sum += int(ISBN[idx])
        else:
            sum += 3*int(ISBN[idx])

ans = 0
if damaged_idx == -1:
    ans = (10-(sum%10))%10
else:
    sum += int(ISBN[12])
    if damaged_idx%2 == 0:
        ans = (10-(sum%10))%10
    else:
        temp_sum = sum
        cnt = 1
        while (10*cnt-(temp_sum%10))%3 != 0:
            cnt += 1
        ans = int(((10*cnt-(temp_sum%10))/3))%10
print(ans)