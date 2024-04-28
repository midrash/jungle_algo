import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
arr_N = [0] * N
arr_M = [0] * M
board = [[0] * M for i in range(N)]

for n in range(N):
    board[n] = list(map(str, input().strip()))
    for m in range(M):
        if board[n][m] == "X":
            arr_N[n] = 1
            arr_M[m] = 1
cnt_M = 0
cnt_N = 0
for i in arr_M:
    if i == 0:
        cnt_M += 1
for i in arr_N:
    if i == 0:
        cnt_N += 1
print(max(cnt_N, cnt_M))
