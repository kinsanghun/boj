n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
result = 0

for num in a:
    result += num * b.pop(b.index(max(b)))

print(result)
