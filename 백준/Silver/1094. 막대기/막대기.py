import sys

n = int(input())
cnt = 0

total = 0

for num in [64, 32, 16, 8, 4, 2, 1]:
    if n == 0 :
        break
    
    if n >= num:
        cnt += 1
        n -= num

print(cnt)
