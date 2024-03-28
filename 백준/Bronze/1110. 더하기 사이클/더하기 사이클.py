import sys
N = int(sys.stdin.readline())

arr = []
if N > 9:
    arr.append(N // 10)
    arr.append(N % 10)
else:
    arr.append(0)
    arr.append(N)
# print(arr)

cnt = 0
while True:
    num = (int(str(arr[cnt])) + int(str(arr[cnt + 1]))) % 10
    arr.append(num)
    # print(num, arr)
    cnt += 1
    # print(int(str(arr[cnt])) + int(str(arr[cnt + 1])))
    if int(str(arr[cnt]) + str(arr[cnt + 1])) == N:
        break
print(cnt)
