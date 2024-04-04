import sys
import heapq
from collections import deque

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]


def draw():
    # for i in range(N):
    #     print(*board[i])
    for i in range(N):
        print(*visited[i])


# draw()

result = []

danjimax = 0


def dfs(y, x, cnt):
    # print(f"단지발견 드가자 y:{i}, x:{j},발견단지 :{cnt}")
    global danjimax
    visited[y][x] = True
    danjimax += 1
    for py, px in drct:
        ty = y + py
        tx = x + px
        if ty >= 0 and ty < N and tx >= 0 and tx < N:
            if visited[ty][tx] == False and board[ty][tx] == 1:
                dfs(ty, tx, cnt + 1)


for i in range(N):
    for j in range(N):
        # print(f"y:{i}, x:{j}, 단진가? :{board[i][j]}, 본적있나? :{visited[i][j]}")
        if (visited[i][j] == False) and (board[i][j] == 1):
            dfs(i, j, 1)
            result.append(danjimax)
            danjimax = 0
            # draw()

print(len(result))
result.sort()
for i in result:
    print(i)
