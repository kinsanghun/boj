a = int(input())
count = 1
current = a//10 + a%10
nxt = a%10

while True:
    if nxt*10 + current%10 == a:
        print(count)
        break
    tmp = current%10
    current = nxt + current%10
    nxt = tmp
    
    count += 1
