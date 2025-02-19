N = int(input())
input_arr = list(map(int, input().split()))

input_arr.sort()
summer = 0
ans = 0
for i in input_arr:
    summer += i
    ans += summer
print(ans)