import sys

n = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cut = [0, 0] # blue, white

def solution(x, y, n):
    color = papers[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if papers[i][j] != color:
                solution(x, y, n//2) # The first piece of quadrant paper
                solution(x, y+n//2, n//2) # The second piece of quadrant paper
                solution(x+n//2, y, n//2) # The third piece of quadrant paper
                solution(x+n//2, y+n//2, n//2) # The fourth piece of quadrant paper
                return
    if color == 0:
        cut[1] += 1
    else:
        cut[0] += 1

    
solution(0, 0, n)

print(cut[1])
print(cut[0])
