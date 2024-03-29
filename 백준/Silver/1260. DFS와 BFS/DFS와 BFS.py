import sys
from collections import deque

# dfsque = deque()
bsdque = deque()

# sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M, V = map(int, input().split())
# print(N, M, V)
check = [False] * (N + 1)

grap = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M):
    l, r = map(int, input().split())
    grap[l][r] = 1
    grap[r][l] = 1


def printgrap():
    for i in range(N + 1):
        print(grap[i])


# printgrap()


def dfs(start):
    check[start] = True
    print(start, end=" ")
    for i in range(1, N + 1):
        if grap[start][i] == 1:
            if check[i] == False:
                dfs(i)


def bfs(start):
    bsdque.append(start)
    # print(check)
    while len(bsdque) > 0:
        num = bsdque.popleft()
        check[num] = True
        print(num, end=" ")
        # print(check)
        for i in range(1, N + 1):
            if grap[num][i] == 1:
                if check[i] == False:
                    bsdque.append(i)
                    check[i] = True
        # print(bsdque)


dfs(V)
print()
check = [False] * (N + 1)
bfs(V)
