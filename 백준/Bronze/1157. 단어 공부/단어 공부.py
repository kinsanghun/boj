string = input()
a = [0 for _ in range(26)]
for s, i in enumerate(string):a[ord(i.upper())-65] += 1
q = max(a);top = a.index(q);a.pop(top)
if max(a) == q:print("?")
else:print(chr(top+65))

