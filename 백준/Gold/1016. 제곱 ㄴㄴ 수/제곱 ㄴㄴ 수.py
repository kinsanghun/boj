import sys

def solution(x, y):
    
    result = y - x + 1
    check = [0] * (y - x + 1)
    
    i=2
    
    while i*i <= y:
        num = i*i
        
        if x % num == 0 : r = 0
        else : r = 1
        
        j = x // num + r
        
        while num*j <= y:
            if not check[num * j - x]:
                check[num * j - x] = 1
                result -= 1
            j+=1
        i+=1
        
    print(result)
    
a, b = map(int,sys.stdin.readline().split())
solution(a,b)
