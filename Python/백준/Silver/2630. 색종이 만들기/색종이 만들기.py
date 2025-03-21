import sys


def divide(n, sr, sc):
    global blue
    global white

    new_arr = []
    for idx in range(sc, sc+n):
        new_arr.append(arr[idx][sr:sr+n])

    sum_of_arr = 0
    for row in new_arr:
        sum_of_arr += sum(row)
    if n == 1:
        if sum_of_arr == 1:
            blue += 1
            return
        else:
            white += 1
            return

    elif sum_of_arr == n**2:
        blue += 1
        return
    elif sum_of_arr == 0:
        white += 1
        return
    else:
        new_n = n // 2
        divide(new_n, sr, sc)
        divide(new_n, sr+new_n, sc)
        divide(new_n, sr, sc+new_n)
        divide(new_n, sr+new_n, sc+new_n)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue = white = 0
divide(N, 0, 0)
print(white)
print(blue)
