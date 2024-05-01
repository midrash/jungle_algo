import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n = int(input())

board = [list(map(str, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]


def draw():
    for i in range(n):
        print(board[i])
    print()


# draw()
def checkCandy():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        # 가로 체크
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        # 세로 체크
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt


result = 1
for i in range(n):
    for j in range(n):
        # 오른스왑
        if j + 1 < n and board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            result = max(result, checkCandy())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        # 아래스왑
        if i + 1 < n and board[i][j] != board[i + 1][j]:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            result = max(result, checkCandy())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(result)