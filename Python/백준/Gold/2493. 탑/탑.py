N = int(input())
arr = list(map(int, input().split()))
ans = [0] * N

stack = list()

idx = 0

while idx < N:
    if len(stack) == 0:
        stack.append([arr[idx], idx])
        idx += 1
        continue
    if arr[idx] < stack[-1][0]:
        ans[idx] = stack[-1][1] + 1
        stack.append([arr[idx], idx])
        idx += 1
    else:
        stack.pop()

print(*ans)
