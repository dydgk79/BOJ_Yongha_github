def square(n):
    while arr[n] == 0:
        arr[n] = square(n-1) + 2*square(n-2)
    return arr[n]


n = int(input())

arr = [0]*1001
arr[1] = 1
arr[2] = 3
arr[3] = 5
square(n)
print(arr[n]%10007)
