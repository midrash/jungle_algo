import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(str, input().strip()))
board = [["."] * N for i in range(N)]


def draw():
    for i in range(N):
        print(*board[i])


def draw2():
    for i in range(N):
        for j in range(N):
            print(board[i][j], end="")
        print()


# draw()
now = [0, 0]
for drc in arr:
    if drc == "R" or drc == "L":
        if drc == "R":
            nx = now[1] + 1
        else:
            nx = now[1] - 1
        if nx >= 0 and nx < N:
            if board[now[0]][now[1]] == ".":
                board[now[0]][now[1]] = "-"
            elif board[now[0]][now[1]] == "|":
                board[now[0]][now[1]] = "+"
            now = [now[0], nx]
            if board[now[0]][now[1]] == ".":
                board[now[0]][now[1]] = "-"
            elif board[now[0]][now[1]] == "|":
                board[now[0]][now[1]] = "+"
    else:
        if drc == "D":
            ny = now[0] + 1
        else:
            ny = now[0] - 1
        if ny >= 0 and ny < N:
            if board[now[0]][now[1]] == ".":
                board[now[0]][now[1]] = "|"
            elif board[now[0]][now[1]] == "-":
                board[now[0]][now[1]] = "+"
            now = [ny, now[1]]
            if board[now[0]][now[1]] == ".":
                board[now[0]][now[1]] = "|"
            elif board[now[0]][now[1]] == "-":
                board[now[0]][now[1]] = "+"
# draw()
draw2()
# print()