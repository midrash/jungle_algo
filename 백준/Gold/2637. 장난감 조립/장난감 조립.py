import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
M = int(input())
board = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
degree[0] == sys.maxsize
cost = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
isDefault = [False] * (N + 1)
for i in range(1, M + 1):
    a, b, c = map(int, input().split())
    board[b].append((a, c))
    degree[a] += 1


def draw():
    for i in range(N + 1):
        print(board[i])
    print()
    print(degree)
    print()
    for i in range(N + 1):
        print(cost[i])


def drawcost():
    print(degree)
    print()
    for i in range(N + 1):
        print(cost[i])


# draw()


def topo():
    que = deque()
    # 간선이 0인 정점들 큐에 넣음
    for i in range(1, N + 1):
        if degree[i] == 0:
            que.append(i)
            isDefault[i] = True
    # print(f"정점이 0인 놈들: {que}")
    # print(f"정점이 0인 놈들: {isDefault}")
    while que:
        now = que.popleft()
        # print(f"이번확인 부품 {now}")
        for toNode, needCost in board[now]:
            # 이번 부품이 기본 부품이면 사용되는 부품에 개수 추가
            # print(f"다른가 {isDefault[now]}")
            if isDefault[now] == True:
                cost[toNode][now] += needCost
            else:
                for i in range(1, N + 1):
                    cost[toNode][i] += cost[now][i] * needCost
            degree[toNode] -= 1
            if degree[toNode] == 0:
                que.append(toNode)
        # drawcost()
    for i in range(1, N + 1):
        if isDefault[i] == True:
            print(f"{i} {cost[N][i]}")


topo()