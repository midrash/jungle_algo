import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
colorCost = []
for i in range(N):
    colorCost.append(list(map(int, input().split())))
board = [[1001] * 3 for _ in range(N)]


def draw():
    # for i in range(N):
    #     print(colorCost[i])
    # print()
    for i in range(N):
        print(board[i])


min_cost = sys.maxsize

# draw()
# for i in range(N):
#     print(colorCost[i])
# print()


for i in range(3):
    board = [[1001] * 3 for _ in range(N)]
    board[0][i] = colorCost[0][i]
    # print(f"i:{i}")
    for j in range(1, N):
        board[j][0] = min(
            colorCost[j][0] + board[j - 1][1], colorCost[j][0] + board[j - 1][2]
        )
        board[j][1] = min(
            colorCost[j][1] + board[j - 1][0], colorCost[j][1] + board[j - 1][2]
        )
        board[j][2] = min(
            colorCost[j][2] + board[j - 1][0], colorCost[j][2] + board[j - 1][1]
        )
    # for j in range(3):
    #     if i == j:
    #         continue
    #     else:
    #         print(f"j:{j}")
    #         print(
    #             f"min_cost: {min_cost}, board[{(j + 1) % 3}]: {board[N - 1][(j + 1) % 3]}, board[{(j + 2) % 3}]: {board[N - 1][(j + 2) % 3]}"
    #         )
    #         min_cost = min(min_cost, board[N - 1][j])
    min_cost = min(min_cost, board[N - 1][(i + 1) % 3], board[N - 1][(i + 2) % 3])
    # draw()

print(min_cost)
