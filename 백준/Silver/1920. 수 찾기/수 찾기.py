N = int(input())
arr = list(map(int, input().split()))
M = int(input())
find_nums = list(map(int, input().split()))

arr.sort()


def findnum(arr, num):
    pl = 0
    pr = len(arr) - 1

    while True:
        pc = (pl + pr) // 2
        if num == arr[pc]:
            print(1)
            return
        elif arr[pc] < num:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            print(0)
            break


for i in find_nums:
    findnum(arr, i)
