input_list = list(map(int, input().split()))

s = 0

for item in input_list:
    s += item*item

s %= 10
print(s)
