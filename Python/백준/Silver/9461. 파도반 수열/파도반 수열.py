arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2
arr[6] = 3


def tri(n):
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = tri(n-1) + tri(n-5)
        return arr[n]

T = int(input())

for _ in range(T):
    N = int(input())
    tri(N)
    print(arr[N])