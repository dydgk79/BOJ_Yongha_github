T = int(input())

for _ in range(T):
    N = int(input())
    category_set = set()
    category_list = []
    num_list = []

    for _ in range(N):
        item, category = input().split()
        if category in category_set:
            idx = category_list.index(category)
            num_list[idx] += 1
        else:
            category_set.add(category)
            num_list.append(1)
            category_list.append(category)

    ans = 1
    for num in num_list:
        ans *= (num+1)
    print(ans-1)