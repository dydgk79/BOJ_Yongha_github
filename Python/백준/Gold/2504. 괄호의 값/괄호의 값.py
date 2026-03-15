arr = input()
stack = list()

ans = 0
temp = 1
for idx in range(len(arr)):
    if arr[idx] == '(':
        stack.append('(')
        temp *= 2
    elif arr[idx] == '[':
        stack.append('[')
        temp *= 3

    elif arr[idx] == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break
        if arr[idx-1] == '(':
            ans += temp
        stack.pop()
        temp //= 2
    elif arr[idx] == ']':
        if not stack or stack[-1] != '[':
            ans = 0
            break
        if arr[idx-1] == '[':
            ans += temp
        stack.pop()
        temp //= 3
if stack:
    ans = 0

print(ans)