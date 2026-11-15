def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    
    dp_0 = [0]*n
    dp_1 = [0]*n
    dp_0[0] = sticker[0]
    dp_1[1] = sticker[1]
    for idx in range(1, n-1):
        dp_0[idx] = max(dp_0[idx-2]+sticker[idx], dp_0[idx-1])
    for idx in range(2, n):
        dp_1[idx] = max(dp_1[idx-2]+sticker[idx], dp_1[idx-1])
    return max(dp_0[n-2], dp_1[n-1])