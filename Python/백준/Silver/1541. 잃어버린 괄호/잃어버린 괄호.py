arr = input()
arr = arr.split('-')

ans = 'initial'
for formula in arr:
    if ans == 'initial':
        ans = 0
        temp_arr = formula.split('+')
        for num in temp_arr:
            ans += int(num)
    else:
        temp_arr = formula.split('+')
        for num in temp_arr:
            ans -= int(num)
print(ans)
