N = int(input())
num = []
num = list(map(int, input().split()))
max_score = max(num)
sum = 0
for idx in range(len(num)):
    num[idx] = (num[idx]/max_score) * 100
    sum += num[idx]
print(sum/N)