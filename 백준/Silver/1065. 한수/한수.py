def hansu(a):
    if a < 100:
        return 1
    c = str(i)
    b = int(c[0]) - int(c[1])
    if b == int(c[1]) - int(c[2]):
        return 1
    return 0

a = int(input())
total = 0
for i in range(1, a+1):
    total += hansu(i)
print(total)