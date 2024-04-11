import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = []
dp = [[0] * N for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))
dp[0][0] = 1


def draw():
    # for i in range(N):
    #     print(board[i])
    # print()
    for i in range(N):
        print(dp[i])
    print()


# draw()

for i in range(N):
    for j in range(N):
        for k in range(1, 10):
            if j - k >= 0:
                if board[i][j - k] == k:
                    dp[i][j] += dp[i][j - k]
            if i - k >= 0:
                if board[i - k][j] == k:
                    dp[i][j] += dp[i - k][j]
print(dp[N - 1][N - 1])
