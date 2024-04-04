import sys
import heapq

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
# print(S, X, Y)


def draw():
    for i in range(N):
        print(*board[i])


# draw()

que = []

for y in range(N):
    for x in range(N):
        if board[y][x] > 0:
            heapq.heappush(que, (board[y][x], y, x, 0))

# print(que)

# print("시작")
while que:
    vc, vy, vx, time = heapq.heappop(que)
    # draw()
    # print(
    #     f"뽑은거 y:{vy}, x:{vx}, 바이러스:{vc % K if (vc % K) > 0 else 3},시간 : {time},  남은que : {que}"
    # )
    # print(f"목적지 y:{X - 1}, x:{Y - 1}, board:{board[X - 1][Y - 1]}")
    # print()
    if board[X - 1][Y - 1] != 0 or time == S:
        print(board[X - 1][Y - 1])
        break
    for py, px in drct:
        ty = vy + py
        tx = vx + px
        if ty >= 0 and ty < N and tx >= 0 and tx < N:
            if board[ty][tx] == 0:
                board[ty][tx] = vc % K if (vc % K) > 0 else 3
                new_time = time + 1
                heapq.heappush(que, (vc + (new_time * K), ty, tx, new_time))