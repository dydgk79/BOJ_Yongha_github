def solution(a):
    answer = 0
    count_dict = {}
    n = len(a)

    for num in a:
        count_dict[num] = count_dict.get(num, 0) + 1

    for num in count_dict:
        if count_dict[num] * 2 <= answer:
            continue

        count = 0
        idx = 0

        while idx < n - 1:
            if (
                a[idx] != a[idx + 1]
                and (a[idx] == num or a[idx + 1] == num)
            ):
                count += 1
                idx += 2
            else:
                idx += 1

        answer = max(answer, count * 2)

    return answer