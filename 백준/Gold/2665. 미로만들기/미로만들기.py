import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
dirct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
floorCnt = 0


def draw():
    for i in range(n):
        print(*board[i])
    for i in range(n):
        print(*visited[i])


# draw()


def bfs(x, y, cost):
    que = deque()
    result = 0
    visited[x][y] = True
    que.append((x, y, cost))
    while que:
        nx, ny, nc = que.popleft()
        if nx == n - 1 and ny == n - 1:
            result = nc
            break
        for px, py in dirct:
            tx = nx + px
            ty = ny + py
            if tx >= 0 and tx < n and ty >= 0 and ty < n and visited[tx][ty] == False:
                visited[tx][ty] = True
                if board[tx][ty] == 1:
                    que.appendleft((tx, ty, nc))
                else:
                    que.append((tx, ty, nc + 1))
    print(result)


bfs(0, 0, 0)
