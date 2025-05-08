import sys
N = int(input())
fruit = list(map(int, sys.stdin.readline().split()))

start_index = 0
searching_index = 1
detecting_index = 0
fruit_set = set()
fruit_set.add(fruit[start_index])
before_fruit = fruit[start_index]
ans = 1
while searching_index < N:
    new_fruit = fruit[searching_index]
    if new_fruit in fruit_set and before_fruit != new_fruit:
        before_fruit = new_fruit
        detecting_index = searching_index
    if new_fruit not in fruit_set:
        fruit_set.add(new_fruit)
        if len(fruit_set) >= 3:
            ans = max(ans, searching_index-start_index)
            start_index = detecting_index
            searching_index = start_index
            fruit_set = set()
            before_fruit = fruit[start_index]
            fruit_set.add(before_fruit)
        else:
            before_fruit = new_fruit
            detecting_index = searching_index
    searching_index += 1
print(max(ans, searching_index-start_index))
