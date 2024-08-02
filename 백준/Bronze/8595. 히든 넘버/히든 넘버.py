import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(str, input().strip()))

flag = False
num = ""
total = 0
for i in range(N):
    if arr[i].isdigit():
        num += arr[i]
        # print(num)
        flag = True
    else:
        if flag:
            total += int(num)
            num = ""
            flag = False

if num.isdigit():
    print(total + int(num))
else:
    print(total)


