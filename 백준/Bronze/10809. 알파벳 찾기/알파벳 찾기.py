string = input()

a = [-1 for _ in range(26)]

for s, i in enumerate(string):
    if a[ord(i)-97] == -1:
        a[ord(i)-97] = s

print(*a)
    
