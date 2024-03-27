import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
blue = 0
white = 0

# for i in range(len(arr)):
#     print(arr[i])


def printpager(sx, sy, n):
    print(f"그림그리러들어옴 sx: {sx}, sy: {sy},n: {n}")
    for i in range(sx, sx + n):
        for j in range(sy, sy + n):
            print(arr[i][j], end=" ")
        print()


def check_paper(sx, sy, n):
    global blue, white
    check = arr[sx][sy]
    # printpager(sx, sy, n)
    if n == 1:
        if check == 1:
            blue += 1
        else:
            white += 1
        # print(f"blue: {blue}, white  {white}")
        return
    # print(f"이번 색깔 {check}")
    else:
        # print(f"sx: {sx} , sy:{sy}, n :{n}")
        flag = True
        for i in range(sx, sx + n):
            for j in range(sy, sy + n):
                # print(f"check: {check}, arr[{i}][{j}]:{arr[i][j]}")
                if arr[i][j] != check:
                    flag = False
                    # print(f"arr[{i}][{j}]:{arr[i][j]}가 색이 다름")
                    break
        if flag == False:
            check_paper(sx, sy, n // 2)
            check_paper(sx + n // 2, sy, n // 2)
            check_paper(sx, sy + n // 2, n // 2)
            check_paper(sx + n // 2, sy + n // 2, n // 2)
        if flag == True:
            if check == 1:
                blue += 1
            else:
                white += 1
            # print(f"blue: {blue}, white  {white}")


check_paper(0, 0, N)
print(f"{white}")
print(f"{blue}")
