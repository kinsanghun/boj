def main():
    l = input()
    handler = 0
    
    for data in l:
        if handler < 0:
            print("NO")
            return
        
        if data == "(":
            handler += 1
        else:
            handler -= 1

    if handler == 0:
        print("YES")
    else:
        print("NO")

count = int(input())

for i in range(count):
    main()
