import sys
N, K = list(map(int, sys.stdin.readline().split()))

arr = []
for i in range(1, N + 1):
    arr.append(i)


cnt = 0
print("<", end="")
while len(arr) > 0:
    cnt += 1
    if len(arr) == 1:
        print(f"{arr[0]}>", end="")
        break
    if cnt == K:
        print(f"{arr[0]}, ", end="")
        cnt = 0
        arr.pop(0)
        # print(f" {arr} ")
        continue
    else:
        temp = arr[0]
        arr.append(temp)
        arr.pop(0)
    # print(arr)
