import sys


def recur(level, start, end):
    if level == 0:
        return
    if start in (1, 2) and end in (1, 2):
        other = 3
    elif start in (2, 3) and end in (2, 3):
        other = 1
    else:
        other = 2
    recur(level-1, start, other)
    start_str = str(start)
    end_str = str(end)
    sys.stdout.write(start_str+" "+end_str+"\n")
    recur(level-1, other, end)


K = int(sys.stdin.readline())
print((1 << K) - 0x1)
recur(K, 1, 3)
