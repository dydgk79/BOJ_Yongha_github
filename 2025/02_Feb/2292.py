N = int(input())
time = 0
while N > 0:
    if time == 0:
        N -= 1
        time += 1
    else:
        N -= 6*time
        time += 1

print(time)