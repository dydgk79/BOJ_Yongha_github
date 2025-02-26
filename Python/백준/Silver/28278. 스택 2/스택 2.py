import sys

N = int(sys.stdin.readline())

stack = []

for idx in range(N):
    order = list(map(int, sys.stdin.readline().split()))
    if len(order) == 2:
        stack.append(order[1])
    elif order[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == 5:
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
