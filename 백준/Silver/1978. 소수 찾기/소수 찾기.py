def solution(n):
    if n == 1:return 0
    for i in range(2, (n//2)+1):
        if n % i == 0: return 0
    return 1

count = 0
input()
for n in list(map(int, input().split())):
    count += solution(n)

print(count)
