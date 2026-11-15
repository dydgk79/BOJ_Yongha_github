def solution(land):
    greedy = [[0]*4 for _ in range(len(land))]
    greedy[0] = land[0]
    
    for idx in range(1, len(land)):
        for num_1 in range(4):
            temp_sum = 0
            for num_2 in range(4):
                if num_1 == num_2:
                    continue
                temp_sum = max(temp_sum, greedy[idx-1][num_2])
            greedy[idx][num_1] = land[idx][num_1] + temp_sum
    return max(greedy[-1])