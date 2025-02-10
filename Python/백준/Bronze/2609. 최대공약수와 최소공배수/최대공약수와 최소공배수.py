A, B = map(int, input().split())

max_multi = 1
for i in range(1, max(A, B)+1):
    if A % i == 0 and B % i == 0:
        max_multi = i
print(max_multi)

min_multi = A*B//max_multi
print(min_multi)