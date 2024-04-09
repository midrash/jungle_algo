import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = []
board = [[0] * (N) for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

# print(arr)


def draw():
    for i in range(N):
        print(board[i])
    print()


# draw()


def dp():
    for i in range(1, N):
        for j in range(N):
            if j + i >= N:
                break
            else:
                if i == 1:
                    # print(
                    #     f"board[{j}][{j+i}]: {arr[j][0]}*{arr[j + 1][0]}*{arr[j + i][1]}"
                    # )
                    board[j][j + i] = arr[j][0] * arr[j + 1][0] * arr[j + i][1]
                else:
                    board[j][j + i] = sys.maxsize
                    for k in range(j, j + i):
                        # print(
                        #     f"board[{j}][{j+i}]: {board[j][k]}+{board[k + 1][j + i]}+{arr[j][0]}*{arr[k + 1][0]}*{arr[j + i][1]}"
                        # )
                        board[j][j + i] = min(
                            board[j][j + i],
                            board[j][k]
                            + board[k + 1][j + i]
                            + arr[j][0] * arr[k + 1][0] * arr[j + i][1],
                        )
        # draw()


dp()
print(board[0][N - 1])