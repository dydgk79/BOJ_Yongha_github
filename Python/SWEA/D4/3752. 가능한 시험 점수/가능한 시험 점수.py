T = int(input())

for t in range(1, T+1):
    answer = 0

    N = int(input())

    scores = list(map(int, input().split()))

    bitmask = 1  # 0점만 가능한 초기 상태
    for s in scores:
        bitmask = bitmask | (bitmask << s)

    # 비트마스크에서 1인 비트 개수 세기
    temp = bitmask
    while temp:
        answer += temp & 1
        temp >>= 1

    print(f"#{t} {answer}")