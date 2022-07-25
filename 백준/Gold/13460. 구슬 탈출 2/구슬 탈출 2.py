def init(graph, n, m):
    rx,ry,bx,by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R': rx, ry = i, j
            if graph[i][j] == 'B': bx, by = i, j
            
    q.append((rx,ry,bx,by,1))
    visited[rx][ry][bx][by] = 1

def move(x, y, dx, dy):
    cnt = 0 
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt +=1
        
    return x, y, cnt

def bfs(graph, n,m):
    init(graph, n,m)
    
    while q:
        rx, ry, bx, by, d = q.popleft()
  
        if d > 10: break
      
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            
            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(d)
                    return
                
                if nrx == nbx and nry == nby:
                    
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                        
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                        
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = 1
                    q.append((nrx, nry, nbx, nby, d+1))
    print(-1)

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    graph = []
    n,m = map(int, input().split())
    for i in range(n):
        temp = list(input().strip())
        graph.append(temp)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    bfs(graph, n, m)
