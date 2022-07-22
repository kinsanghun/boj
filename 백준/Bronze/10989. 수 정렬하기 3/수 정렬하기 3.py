import sys
n = int(sys.stdin.readline())
l = [0] * 10001

for _ in range(n):
    m = int(sys.stdin.readline())
    l[m] += 1

for i in range(len(l)):
    if l[i]:
        for _ in range(l[i]):
            print(i)