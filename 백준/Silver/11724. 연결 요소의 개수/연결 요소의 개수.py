import sys
from collections import deque
sys.setrecursionlimit(10**9)
# dfsque = deque()
# bsdque = deque()

# sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
# print(N, M)
board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
check = [False] * (N + 1)
for i in range(M):
    n, r = map(int, input().split())
    board[n][r] = 1
    board[r][n] = 1


def printboard():
    for i in range(N + 1):
        print(board[i])


# printboard()

cnt = 0


def dfs(v):
    global cnt
    check[v] = True
    for i in range(1, N + 1):
        if board[v][i] == 1 and check[i] == False:
            check[v] = True
            dfs(i)


for i in range(1, N + 1):
    # print(check)
    if check[i] == False:
        dfs(i)
        cnt += 1

print(cnt)
