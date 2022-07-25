import sys

n = int(input())
ropes = [int(sys.stdin.readline()) for _ in range(n)]
used = 1
ropes.sort()
total = 0
check = 0
for rope in reversed(ropes):
    check = rope * used
    used += 1
    if total < check:
        total = check

print(total)
    
