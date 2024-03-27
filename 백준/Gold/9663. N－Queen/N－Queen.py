import sys
N = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chesboard = [[0 for j in range(N)] for i in range(N)]
# for i in range(N):
#     for j in range(N):
#         chesboard[i][j] = 0
# chesboard = [[1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 1]]


def drawboard(checkarr):
    for i in range(N):
        print(chesboard[i])
    print(checkarr)


checkarr = [False] * N
# drawboard(checkarr)

cnt = 0


def isQueen(idx, depth, checkarr):
    # drawboard(checkarr)
    # print(f"놓은 위치 :{idx}, 깊이 {depth}")

    if depth == 0:
        return True
    for i in range(1, depth + 1):
        if checkarr[idx] == True:
            # print(f"같은열 chesboard[{depth - i}],[{idx}]실패 돌아가!")
            return False
        if idx - i >= 0:
            if chesboard[depth - i][idx - i] == 1:
                # print(f"좌 대각선 chesboard[{depth - i}],[{idx - i}]실패 돌아가!")
                return False
        if idx + i < N:
            if chesboard[depth - i][idx + i] == 1:
                # print(f"우 대각선 chesboard[{depth - i}],[{idx + i}]실패 돌아가!")
                return False
    return True


def queen(depth, checkarr):
    global cnt
    if depth >= N:
        cnt += 1
        # drawboard(checkarr)
        return
    for i in range(N):
        can = isQueen(i, depth, checkarr)
        if can:
            # print(f"depth: {depth}")
            chesboard[depth][i] = 1
            checkarr[i] = True
            depth += 1
            # drawboard(checkarr)
            queen(depth, checkarr)
            depth -= 1
            chesboard[depth][i] = 0
            checkarr[i] = False
            # drawboard(checkarr)


queen(0, checkarr)
print(cnt)