import sys

Q = int(sys.stdin.readline())
data = dict()

for _ in range(Q):
    order, coor = map(int, sys.stdin.readline().split())
    if order == 1:
        temp_height = 0
        for idx in range(coor,coor+4):
            if idx in data:
                temp_height = max(temp_height, data.get(idx))
        for idx in range(coor,coor+4):
            data[idx] = temp_height + 1
    elif order == 2:
        temp_height = 4
        if coor in data:
            temp_height += data.get(coor)
        data[coor] = temp_height
    elif order == 3:
        if coor in data:
            sys.stdout.write(str(data.get(coor))+'\n')
        else:
            sys.stdout.write('0'+'\n')