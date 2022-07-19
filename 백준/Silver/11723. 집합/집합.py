import sys

bitmask = 0
cnt = int(input())

for _ in range(cnt):
    i = sys.stdin.readline().split()
    
    if i[0] == "add":
        i[1] = int(i[1])
        if ((bitmask >> (i[1]-1)) & 1) == 1:continue
        bitmask |= 1 << (i[1]-1)
    elif i[0] == "remove":
        i[1] = int(i[1])
        if ((bitmask >> (i[1]-1)) & 1) == 0:continue
        bitmask ^= 1 << (i[1]-1)
    elif i[0] == "check":
        i[1] = int(i[1])
        if ((bitmask >> (i[1]-1)) & 1) == 1:print(1)
        else : print(0)
    elif i[0] == "toggle":
        i[1] = int(i[1])
        bitmask ^= 1 << (i[1]-1)
    elif i[0] == "all":bitmask = 2**20-1
    elif i[0] == "empty":
        bitmask = 0
