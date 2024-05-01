import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
colorCost = []
for i in range(N):
    colorCost.append(list(map(int, input().split())))
board = [[0] * 3 for _ in range(N)]
board[0] = colorCost[0]


def draw():
    for i in range(N):
        print(colorCost[i])
    print()
    for i in range(N):
        print(board[i])


# draw()
for i in range(1, N):

    board[i][0] = min(
        colorCost[i][0] + board[i - 1][1], colorCost[i][0] + board[i - 1][2]
    )
    board[i][1] = min(
        colorCost[i][1] + board[i - 1][0], colorCost[i][1] + board[i - 1][2]
    )
    board[i][2] = min(
        colorCost[i][2] + board[i - 1][0], colorCost[i][2] + board[i - 1][1]
    )
# print()
# draw()
print(min(board[N - 1][0], board[N - 1][1], board[N - 1][2]))