TC = int(input())

for _ in range(TC):
    N, S = input().split()
    N = int(N)

    answer = 0

    for i in range(N):
        count_a = 0
        count_t = 0
        count_c = 0
        count_g = 0

        for j in range(i, N):
            if S[j] == 'A':
                count_a += 1
            elif S[j] == 'T':
                count_t += 1
            elif S[j] == 'C':
                count_c += 1
            elif S[j] == 'G':
                count_g += 1

            if count_a == count_t and count_c == count_g:
                answer += 1

    print(answer)