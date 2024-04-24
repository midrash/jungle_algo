import sys
sys.setrecursionlimit(10**9)
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
board = []
# visited = [[0] * N for _ in range(N)]
min_ = sys.maxsize
max_ = -sys.maxsize
max_cnt = -sys.maxsize
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in board[i]:
        if max_ < j:
            max_ = j
        if min_ > j:
            min_ = j
# print(f"min: {min_}, max: {max_}")


def draw():
    # for i in range(N):
    #     print(board[i])
    print()
    for i in range(N):
        print(visited[i])


# draw()


def dfs(y, x, cnt, water):
    global visited
    visited[y][x] = cnt
    for dy, dx in direction:
        ny = dy + y
        nx = dx + x
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if visited[ny][nx] == 0 and board[ny][nx] > water:
                dfs(ny, nx, cnt, water)


for water in range(max_):
    # 방문 초기화
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0 and board[y][x] > water:
                cnt += 1
                dfs(y, x, cnt, water)
    if max_cnt < cnt:
        max_cnt = cnt
    # draw()
    # print(f"max_cnt: {max_cnt}")
    # print()
print(max_cnt)
