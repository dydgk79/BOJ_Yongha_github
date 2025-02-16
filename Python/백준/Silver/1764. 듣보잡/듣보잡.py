import sys

N, M = map(int, sys.stdin.readline().split())  # 빠른 입력 사용
nset = set(sys.stdin.readline().strip() for _ in range(N))  # set 사용
mset = set(sys.stdin.readline().strip() for _ in range(M))

result = sorted(nset & mset)  # 교집합을 정렬

print(len(result))
print("\n".join(result))  # 출력 최적화
