A, B, V = map(int, input().split())

last_height = V-A
until_rise = last_height // (A-B)
if until_rise*(A-B) + A >= V:
    print(until_rise+1)
else:
    print(until_rise+2)