def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        
def fibonacci(n):
    f = [1] * (n+1)
    cnt = 0
    for i in range(3,n+1):
        cnt+=1
        f[i]=f[i-1] + f[i-2]
    return cnt

n = int(input())
print(fib(n),fibonacci(n))