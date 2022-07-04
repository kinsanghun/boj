c = int(input())
l = list()
for i in range(c):
    l.append(input())

for d in l:
    t = 0
    v = 1
    for a in d:
        if a == "X":
            v = 1
        else:
            t += v
            v += 1
    print(t)
