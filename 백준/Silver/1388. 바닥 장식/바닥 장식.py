import sys
import heapq
from collections import deque

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(str, input().strip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]


def draw():
    # for i in range(N):
    #     print(*board[i])
    for i in range(N):
        print(*visited[i])


# draw()

cnt = 0


def dfs(y, x, check):
    visited[y][x] = True
    if board[y][x] == "-":
        nx = x + 1
        if (nx < M) and (board[y][nx] == check):
            dfs(y, nx, check)
    elif board[y][x] == "|" and board[y][x] == check:
        ny = y + 1
        if (ny < N) and (board[ny][x] == check):
            dfs(ny, x, check)


for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            # print(f"이번 스타트 y:{i} x:{j}")
            wood = board[i][j]
            dfs(i, j, wood)
            cnt += 1
            # draw()
            # print(f"올린다 나무 {cnt}")
            # print()

print(cnt)
