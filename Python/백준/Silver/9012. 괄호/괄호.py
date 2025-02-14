T = int(input())

for _ in range(T):
    input_ps = input()
    ans = 'YES'
    n = len(input_ps)
    stack = []
    top = -1
    for item in input_ps:
        if item == '(':
            stack.append(item)
            top += 1
        elif item == ')':
            if top == -1:
                ans = 'NO'
                break
            else:
                top -= 1
                stack.pop()
    if stack:
        ans = 'NO'
    print(ans)
