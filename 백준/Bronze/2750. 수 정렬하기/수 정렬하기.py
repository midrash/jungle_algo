N = int(input())

arr = [int(input()) for _ in range(N)]

min = 1001
while len(arr) > 0:
    for i, val in enumerate(arr):
        if min > val:
            min = val
            check = i
    print(arr[check])
    del arr[check]
    min = 1001
