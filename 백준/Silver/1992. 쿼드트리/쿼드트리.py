import sys
N = int(sys.stdin.readline())
arrs = []
for i in range(N):
    arrs.append(list(map(int, input())))
ansser = []


def printpager(sx, sy, n):
    print(f"그림그리러들어옴 sx: {sx}, sy: {sy},n: {n}")
    for i in range(sx, sx + n):
        for j in range(sy, sy + n):
            print(arrs[i][j], end=" ")
        print()


def drawanswer():
    for i in ansser:
        print(i, end="")
    print()


def check(x, y, n):
    # printpager(x, y, n)
    if n == 1:
        return True
    checknum = arrs[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if checknum != arrs[i][j]:
                return False
    return True


def qt(sx, sy, n):
    num = arrs[sx][sy]
    result = check(sx, sy, n)
    if result == True:
        ansser.append(str(num))
        # print(f"성공: {num} 추가")
        # drawanswer()
    else:
        ansser.append("(")
        qt(sx, sy, n // 2)
        qt(sx, sy + n // 2, n // 2)
        qt(sx + n // 2, sy, n // 2)
        qt(sx + n // 2, sy + n // 2, n // 2)
        ansser.append(")")


qt(0, 0, N)
drawanswer()
