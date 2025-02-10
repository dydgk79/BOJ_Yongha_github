L = int(input())
arr = input()
sum = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for idx in range(L):
    input_alpha = arr[idx]
    input_num = alphabet.index(input_alpha)+1
    result = input_num
    for i in range(idx):
        result *= 31
    sum += result
print(sum)