import sys

n = int(input())
students = []

for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    students.append((w, h))

for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]: rank += 1
    print(rank, end = " ")