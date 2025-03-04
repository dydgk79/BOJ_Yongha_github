from itertools import combinations


def checker(x):
    vowel = ['a', 'e', 'i', 'o', 'u']
    v_cnt = 0
    c_cnt = 0
    for idx in range(len(x)):
        if x[idx] in vowel:
            v_cnt += 1
        else:
            c_cnt += 1
    if v_cnt >= 1 and c_cnt >= 2:
        return True
    else:
        return False


L, C = map(int, input().split())
pwd_list = list(input().split())
pwd_list.sort()
part_set = list(combinations(pwd_list,L))
for idx in range(len(part_set)):
    ans = "".join(part_set[idx])
    if checker(ans):
        print(ans)
