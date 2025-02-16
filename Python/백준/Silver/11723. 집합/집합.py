import sys

S = set()
M = int(sys.stdin.readline())  # 빠른 입력

for _ in range(M):
    command = sys.stdin.readline().strip().split()  # 입력 한 줄 읽고 분리
    if len(command) == 2:
        order, digit = command[0], int(command[1])
    else:
        order = command[0]

    if order == 'add':
        S.add(digit)
    elif order == 'remove':
        S.discard(digit)  # 존재하지 않는 경우 에러 방지
    elif order == 'check':
        print("1" if digit in S else "0")
    elif order == 'toggle':
        if digit in S:
            S.remove(digit)
        else:
            S.add(digit)
    elif order == 'all':
        S = set(range(1, 21))
    elif order == 'empty':
        S.clear()
