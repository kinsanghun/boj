import sys

n, k = map(int, sys.stdin.readline().split())

queue = [i for i in range(1, n + 1)]
temp = []
index = 0

while queue:
    index += k - 1
    if index >= len(queue):index %= len(queue)
    temp.append(str(queue.pop(index)))

print("<", ", ".join(temp), ">", sep="")