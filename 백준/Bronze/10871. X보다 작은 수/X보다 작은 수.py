a, b = map(int, input().split())
l = map(int, input().split())

for data in l:
    if b > data:
        print(data, end=" ")