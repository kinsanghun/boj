import sys
a,b,c = map(int,sys.stdin.readline().split())

def solution(a, b):
    if b == 1: return a % c
    n = solution(a, b//2)
    if b % 2: return (n  * n * a) % c
    else: return (n * n) % c
          
print(solution(a,b))
