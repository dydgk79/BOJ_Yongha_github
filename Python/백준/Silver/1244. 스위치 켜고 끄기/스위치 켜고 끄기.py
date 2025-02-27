N = int(input())

switch_list = list(map(int, input().split()))

S = int(input())


def switch_convert(i):
    if switch_list[i] == 1:
        switch_list[i] = 0
    else:
        switch_list[i] = 1


def boy(x):
    for idx in range(N):
        if (idx+1) % x == 0:
            switch_convert(idx)


def girl(x):
    idx = x-1
    switch_convert(idx)
    k = 1
    while 0<=idx-k and idx+k<N:
        if switch_list[idx-k] == switch_list[idx+k]:
            switch_convert(idx-k)
            switch_convert(idx+k)
            k += 1
        else:
            return


for _ in range(S):
    input_data = list(map(int, input().split()))
    if input_data[0] == 1:
        boy(input_data[1])
    else:
        girl(input_data[1])

cnt = 0
while switch_list:
    print(switch_list.pop(0), end=" ")
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0

