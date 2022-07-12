a = int(input())
for i in range(a):
    tmp = input().split()
    for z in tmp[1]:
        print(z*int(tmp[0]),end="")
    print()
