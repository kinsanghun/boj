import sys

n = int(input())

times = list()
for _ in range(n):
    times.append(list(map(int, sys.stdin.readline().split())))


times.sort(key = lambda x: (x[1], x[0]))

count = 1
now = times[0][1]

for time in times[1:]:
    if now <= time[0]:
        now = time[1]
        count += 1

print(count)
