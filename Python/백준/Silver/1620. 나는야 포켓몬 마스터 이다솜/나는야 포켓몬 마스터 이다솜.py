import sys

N, M = map(int, sys.stdin.readline().split())  # 빠른 입력

poke_list_num = {}  # 숫자로 찾기
poke_list_name = {}  # 이름으로 찾기

for idx in range(1, N + 1):  # 포켓몬 정보 저장
    poke_name = sys.stdin.readline().strip()
    poke_list_num[idx] = poke_name  # 숫자로 이름 찾기
    poke_list_name[poke_name] = idx  # 이름으로 숫자 찾기

output = sys.stdout.write  # 빠른 출력

for _ in range(M):  # 문제 질문
    q = sys.stdin.readline().strip()
    if q.isdigit():
        output(poke_list_num[int(q)] + "\n")  # 숫자로 이름 찾기
    else:
        output(str(poke_list_name[q]) + "\n")  # 이름으로 숫자 찾기
