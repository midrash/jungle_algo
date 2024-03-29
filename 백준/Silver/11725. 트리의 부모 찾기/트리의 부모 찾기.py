import sys
from collections import deque

# dfsque = deque()
# bsdque = deque()

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
# M = int(input())
# print(N, M)
board = [[] for _ in range(N + 1)]
check = [False] * (N + 1)
parrent = [0] * (N + 1)
for i in range(N - 1):
    n, r = map(int, input().split())
    board[n].append(r)
    board[r].append(n)


def printboard():
    for i in range(N + 1):
        print(board[i])


# printboard()


def dfs(v):
    check[v] = True
    # print(board[v])
    for i in board[v]:
        if check[i] == False:
            parrent[i] = v
            dfs(i)


dfs(1)
for i in range(2, len(parrent)):
    print(parrent[i])

