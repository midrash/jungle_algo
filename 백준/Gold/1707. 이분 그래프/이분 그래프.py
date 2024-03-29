import sys
from collections import deque

# dfsque = deque()
# bsdque = deque()

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
K = int(input())
# M = int(input())
# print(N, M)


def printboard():
    for i in range(N + 1):
        print(board[i])


def dfs(v, nowcolor, V):
    check[v] = True
    color[v] = nowcolor
    # print(f" 이번 점:{v}, 이번색깔 :{nowcolor}")
    # print(check)
    result = True
    for i in board[v]:
        # print(f"비교색깔 :{color[i]}")
        if color[i] == nowcolor:
            result = False
        elif check[i] == False:
            result = dfs(i, (nowcolor + 1) % 2, V)
    return result


def printboard(s):
    for i in range(s + 1):
        print(board[i])


for _ in range(K):
    V, E = map(int, input().split())
    board = [[] for _ in range(V + 1)]
    check = [False] * (V + 1)
    color = [None] * (V + 1)
    for i in range(E):
        l, r = map(int, input().split())
        board[l].append(r)
        board[r].append(l)
    # printboard(V)
    result = True
    for i in range(1, V):
        # print()
        if check[i] == False:
            result = dfs(i, 0, V)
            if result == False:
                break
    if result:
        print("YES")
    else:
        print("NO")

    # print("하나 끝")


def printboard(s):
    for i in range(s):
        print(board[i])
