import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
# print(N, M)
derection = [(0, 1), (1, 0), (-1, 0), (0, -1)]

board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
max = sys.maxsize


def drawboard():
    for i in range(N):
        print(board[i])
    for i in range(N):
        print(visited[i])


# drawboard()


## dfs는 틀렸다고 나오는데 시간초과 나오나봄
# def dfs(y, x, cnt):
#     global max
#     if cnt + 1 >= max:
#         return
#     # print(f"이번 위치 [{y}][{x}]")
#     if y == N - 1 and x == M - 1:
#         # print(f"도착했다. {cnt}만큼 걸렸어")
#         if cnt < max:
#             max = cnt
#         return
#     visited[y][x] = True

#     for i in range(4):
#         ly = y + derection[i][0]
#         lx = x + derection[i][1]
#         # print(
#         #     f"체크 [{ly}][{lx}] , 방문여부 : {visited[ly][lx]}, 벽여부 : {board[ly][lx]}"
#         # )
#         if (
#             ly >= 0
#             and ly < N
#             and lx >= 0
#             and lx < M
#             and visited[ly][lx] == False
#             and board[ly][lx] == 1
#         ):

#             dfs(ly, lx, cnt + 1)


# dfs(0, 0, 1)


def bfs(y, x, cnt):
    global max
    que = deque()
    visited[y][x] = True
    que.append((y, x, cnt))
    while len(que) > 0:
        now = que.popleft()
        # print(f"이번 위치 [{now[0]}][{now[1]}], cnt : {cnt}]")
        if now[0] == N - 1 and now[1] == M - 1:
            # print(f"도착했다. {now[2]}만큼 걸렸어")
            if now[2] < max:
                max = now[2]
            return
        for i in range(4):
            ly = now[0] + derection[i][0]
            lx = now[1] + derection[i][1]
            lcnt = now[2] + 1
            # print(
            #     f"체크 [{ly}][{lx}] , 방문여부 : {visited[ly][lx]}, 벽여부 : {board[ly][lx]}"
            # )
            if (
                ly >= 0
                and ly < N
                and lx >= 0
                and lx < M
                and visited[ly][lx] == False
                and board[ly][lx] == 1
            ):
                # print(f"다음갈꺼 [{ly}][{lx}, cnt : {cnt + 1}]")
                visited[ly][lx] = True
                que.append((ly, lx, lcnt))


bfs(0, 0, 1)
print(max)
