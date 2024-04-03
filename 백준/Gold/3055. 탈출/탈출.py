import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R, C = map(int, input().split())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
# board = [list(map(str, input().split())) for _ in range(R)]
gosumx = 0
gosumy = 0
que_gosum = deque()
que_water = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == "*":
            visited[i][j] = 2
            que_water.append((i, j))
        elif board[i][j] == "X":
            visited[i][j] = 3
        elif board[i][j] == "D":
            visited[i][j] = 4
        elif board[i][j] == "S":
            visited[i][j] = 1
            gosumx = j
            gosumy = i
            que_gosum.append((i, j, 0))


def draw():
    print(f"지도")
    for i in range(R):
        print(*board[i])
    print(f"숫자지도")
    for i in range(R):
        print(*visited[i])


# draw()


def bfs():
    global que_gosum, que_water
    while que_gosum or que_water:
        # 물부터 진행
        for _ in range(len(que_water)):
            nwy, nwx = que_water.popleft()
            # print(f"이번 물의 위치 y:{nwy}, x:{nwx}")
            for py, px in direct:
                twy = nwy + py
                twx = nwx + px
                if (
                    twy >= 0
                    and twy < R
                    and twx >= 0
                    and twx < C
                    and visited[twy][twx] < 2
                ):
                    visited[twy][twx] = 2
                    que_water.append((twy, twx))
        # 고슴이는 물 다음에 진행
        for _ in range(len(que_gosum)):
            ngy, ngx, ngc = que_gosum.popleft()
            # print(f"이번 고슴의 위치 y:{ngy}, x:{ngx}, 이동횟수 {ngc}")
            for py, px in direct:
                tgy = ngy + py
                tgx = ngx + px

                if tgy >= 0 and tgy < R and tgx >= 0 and tgx < C:
                    if board[tgy][tgx] == "D":
                        # print(f"고슴이 탉출 {ngc + 1}")
                        return ngc + 1
                    elif visited[tgy][tgx] < 1:
                        visited[tgy][tgx] = 1
                        que_gosum.append((tgy, tgx, ngc + 1))
        # print(f"진행상황")
        # for i in range(R):
        #     print(*visited[i])
    return False


result = bfs()
if result == False:
    print("KAKTUS")
else:
    print(result)
