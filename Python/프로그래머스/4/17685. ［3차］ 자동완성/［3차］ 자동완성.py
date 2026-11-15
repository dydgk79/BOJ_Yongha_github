def solution(words):
    answer = 0
    words.sort()

    def compare_letter(word1, word2):
        count = 0

        for idx in range(min(len(word1), len(word2))):
            if word1[idx] != word2[idx]:
                break
            count += 1

        return count

    for idx in range(len(words)):
        word = words[idx]

        if idx == 0:
            nxt_word = words[idx + 1]
            answer += min(len(word), compare_letter(word, nxt_word) + 1)

        elif idx == len(words) - 1:
            bfr_word = words[idx - 1]
            answer += min(len(word), compare_letter(word, bfr_word) + 1)

        else:
            nxt_word = words[idx + 1]
            bfr_word = words[idx - 1]

            nxt_count = compare_letter(word, nxt_word)
            bfr_count = compare_letter(word, bfr_word)

            answer += min(len(word), max(nxt_count, bfr_count) + 1)

    return answer