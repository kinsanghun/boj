import sys

n = int(input())
m = int(input())

visited = [0 for _ in range(n+1)]
l = [[0] for _ in range(n+1)]

cnt = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

def dfs(start):
    global cnt
    if visited[start]:
        return
    
    cnt += 1
    visited[start] = start

    for nextNode in l[start]:
        if nextNode not in visited:
            dfs(nextNode)

dfs(1)
print(cnt-1)
