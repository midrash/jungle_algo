import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [[1] * 3 for _ in range(N)]

for i in range(1, N):
    arr[i][0] = (arr[i - 1][1] + arr[i - 1][2])%9901
    arr[i][1] = (arr[i - 1][0] + arr[i - 1][2])%9901
    arr[i][2] = (arr[i - 1][0] + arr[i - 1][1] + arr[i - 1][2])%9901

print((arr[N - 1][0] + arr[N - 1][1] + arr[N - 1][2])%9901)
