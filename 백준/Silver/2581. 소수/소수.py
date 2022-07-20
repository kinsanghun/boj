def solution(n):
    if n == 1:return 0
    for i in range(2, (n//2)+1):
        if n % i == 0: return 0
    return n

count = 0
q = 0
t = 0
a = int(input())
b = int(input())

for n in range(a, b+1):
    count += solution(n)
    if count != 0 and q == 0:
        q = 1
        t = n

if count:
    print(count)
    print(t)
else:
    print(-1)
