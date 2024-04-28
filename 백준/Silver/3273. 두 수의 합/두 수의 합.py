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
        li += 1
    elif arr[li] + arr[ri] > x:
        ri -= 1
    else:
        li += 1
print(cnt)
