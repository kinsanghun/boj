import sys

i = int(input())

for n in range(i):    
    a, b = map(int, (sys.stdin.readline().rstrip()).split())
    print(a + b)
