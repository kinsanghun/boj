from sys import stdin, stdout

c = stdin.readline()
l = sorted(map(int,stdin.readline().split()))

n = stdin.readline()
s = map(int, stdin.readline().split())

def search_(arr, wanted, start, end):
    c = (end + start) // 2
    
    if arr[c] == wanted:
        return 1
    
    elif end - start <= 1:
        return 0
    
    else:
        if arr[c] > wanted:
            return search_(arr, wanted, start, c)
        else:
            return search_(arr, wanted, c, end)

length = len(l)

for i in s:
    print(search_(l, i, 0, length))
    
