T = int(input())

for test_case in range(1, 1+T):
    k = int(input())
    n = int(input())

    residence_arr = [[0]*(n) for _ in range(k+1)]

    for i in range(n):
        residence_arr[0][i] = i+1
    for i in range(1, k+1):
        resi_sum = 1
        for j in range(n):
            if j != 0:
                resi_sum += residence_arr[i - 1][j]
            residence_arr[i][j] = resi_sum

    print(residence_arr[k][n-1])

