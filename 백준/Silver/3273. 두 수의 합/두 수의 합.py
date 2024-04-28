import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
arr.sort()
li = 0
ri = len(arr) - 1
while li < ri:
    if arr[li] + arr[ri] == x:
        cnt += 1
        while (li + 1 <= ri) and (arr[li] == arr[li + 1]):
            # print("여긴가?1")
            cnt += 1
            li += 1
        while (ri - 1 >= li) and (arr[ri] == arr[ri - 1]):
            # print("여긴가?1")
            cnt += 1
            ri -= 1
        if (li + 1 <= ri) and arr[li] != arr[li + 1]:
            li += 1
        if (ri - 1 >= li) and arr[ri] != arr[ri - 1]:
            ri -= 1
    elif arr[li] + arr[ri] > x:
        ri -= 1
    else:
        li += 1
print(cnt)
