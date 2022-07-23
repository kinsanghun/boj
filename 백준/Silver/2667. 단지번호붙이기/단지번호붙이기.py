import sys

n = int(input())

graph = list()

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

b = 0
cnt = 0
result = list()

def solution(y, x):
    global cnt
    
    graph[y][x] = 0
    cnt += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or ny >= n or nx >= n : continue

        if graph[ny][nx]:
            solution(ny, nx)

for g in range(n):
    for i in range(n):
        if graph[g][i]:
            b += 1
            cnt = 0
            solution(g, i)
            result.append(cnt)

result.sort()

print(b)
for r in result:
    print(r)
