from collections import deque
import sys

N = int(input())
stack = deque()
top = -1

for _ in range(N):
    input_order = sys.stdin.readline().split()
    if input_order[0] == 'push':
        stack.append(input_order[1])
        top += 1
    elif input_order[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif input_order[0] == 'size':
        print(top+1)
    elif input_order[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif stack:
        print(stack[top])
    else:
        print(top)
