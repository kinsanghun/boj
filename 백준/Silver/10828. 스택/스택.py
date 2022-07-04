import sys
s = []
n = int(sys.stdin.readline())
for i in range(n):
    c = sys.stdin.readline().split()
    q = c[0]
    l = len(s)
    if "u" in q: s.append(int(c[1]))
    elif "y" in q: print("0" if l else "1")
    elif "z" in q: print(l)
    elif "t" in q: print(s[-1] if l else "-1")
    else: print(s.pop() if l else "-1")

