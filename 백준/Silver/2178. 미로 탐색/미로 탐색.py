from collections import deque

n, m = map(int, input().split())
graph = list()
visited = list()

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append((y, x))
    visited.append((y, x))
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or ny >= n or nx >= m :continue

            if graph[ny][nx] == 1 and (ny, nx) not in visited:
                graph[ny][nx] = graph[y][x] + 1
                visited.append((ny, nx))
                queue.append((ny, nx))

    return graph[n - 1][m - 1]

print(dfs(0, 0))