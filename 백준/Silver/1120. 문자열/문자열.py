import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

arr = list(map(str, input().split()))
arr[0] = list(arr[0].strip())
arr[1] = list(arr[1].strip())
# print(arr)
cnt = 0
min_cnt = 99999
for i in range(len(arr[1]) - len(arr[0]) + 1):
    # print(f"I:{i}")
    for j in range(len(arr[0])):
        if arr[0][j] != arr[1][i + j]:
            # print(f"A:{arr[0][j]}, B:{arr[1][i + j]}")
            cnt += 1
    if cnt < min_cnt:
        min_cnt = cnt
    # print(f"cnt:{cnt}")
    cnt = 0
    # print()
print(min_cnt)
