while True:
    input_num = input()
    if input_num == '0':
        break
    else:
        length = len(input_num)
        answer = 'yes'
        if length % 2 == 0:
            for idx in range(int(length)):
                if input_num[idx] != input_num[int(length - idx - 1)]:
                    answer = 'no'
        else:
            for idx in range(int(length - 1)):
                if input_num[idx] != input_num[int(length - idx - 1)]:
                    answer = 'no'
        print(answer)
