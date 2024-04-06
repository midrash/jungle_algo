import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [(0, 0)] * (N + 1)
for i in range(1, N + 1):
    weight, happy = map(int, input().split())
    bag[i] = (weight, happy)

bag.sort()
# print(N, K, bag)

board = [[0] * (K + 1) for _ in range(N + 1)]


def draw():
    for i in range(N + 1):
        print(board[i])


# draw()


def dp():
    for i in range(1, len(bag)):
        # print(f"이번 물건 i:{i}, 무게:{bag[i][0]},가치:{bag[i][1]}, ")
        for j in range(K + 1):
            if j < bag[i][0]:
                board[i][j] = board[i - 1][j]
            else:
                board[i][j] = max(
                    board[i - 1][j], board[i - 1][j - bag[i][0]] + bag[i][1]
                )
        # draw()


dp()
print(board[N][K])
