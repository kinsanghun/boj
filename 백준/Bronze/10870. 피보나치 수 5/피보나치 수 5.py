def pbnc(b=0, a=1, c=0):
    if c == 0: return b
    return pbnc(b=a, a=a+b, c=c-1)

a = int(input())
print(pbnc(c=a))