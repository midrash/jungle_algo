import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

str1 = list(map(str, input().strip()))
str2 = list(map(str, input().strip()))
# print(str1)
# print(str2)
str1len = len(str1)
str2len = len(str2)
board = [[0] * (str1len + 1) for _ in range(str2len + 1)]


def draw():
    for i in range(str2len + 1):
        print(board[i])


# draw()
cnt = 0
for i in range(1, str2len + 1):
    for j in range(1, str1len + 1):
        # print(f"i: {i}, j: {j}")
        if str1[j - 1] == str2[i - 1]:
            board[i][j] = board[i - 1][j - 1] + 1
        else:
            board[i][j] = max(board[i - 1][j], board[i][j - 1])
# draw()

print(board[str2len][str1len])
