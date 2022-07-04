import sys

i = int(input())

for n in range(1, i+1):    
    a, b = map(int, (sys.stdin.readline().rstrip()).split())
    print(f"Case #{n}: {a + b}")
