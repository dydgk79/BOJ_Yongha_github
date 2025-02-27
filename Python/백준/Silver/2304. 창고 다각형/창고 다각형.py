N = int(input())

pillar = [0]*1001

largest_L = -float('inf')
tallest_H = -float('inf')
tallest_L = 0
for _ in range(N):
    L, H = map(int, input().split())
    pillar[L] = H
    largest_L = max(largest_L, L)
    if tallest_H < H:
        tallest_H = H
        tallest_L = L

ziped_pillar = pillar[:largest_L+1]

area = 0

tallest_height = -float('inf')
for idx in range(tallest_L):
    if tallest_height < ziped_pillar[idx]:
        tallest_height = ziped_pillar[idx]
    area += tallest_height

tallest_height = -float('inf')
for idx in range(largest_L,tallest_L,-1):
    if tallest_height < ziped_pillar[idx]:
        tallest_height = ziped_pillar[idx]
    area += tallest_height
area += tallest_H
print(area)
