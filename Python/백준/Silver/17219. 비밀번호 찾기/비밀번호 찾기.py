import sys

N, M = map(int, sys.stdin.readline().split())
password = dict()
for _ in range(N):
    k, v = sys.stdin.readline().split()
    password[k] = v
for _ in range(M):
    key = input()
    sys.stdout.write(password.get(key))
    print()