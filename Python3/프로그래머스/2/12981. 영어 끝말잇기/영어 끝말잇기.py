def solution(n, words):
    answer = [0,0]
    word_set = set()
    word_set.add(words[0])
    
    for idx in range(1, len(words)):
        if words[idx] in word_set:
            answer = [(idx%n)+1, (idx//n)+1]
            break
        if words[idx][0] != words[idx-1][-1]:
            answer = [(idx%n)+1, (idx//n)+1]
            break
        
        word_set.add(words[idx])
    return answer