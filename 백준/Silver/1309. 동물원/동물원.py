import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [[1] * 2]
i = 1
while i < N:
    temp = arr[0][0]
    arr[0][0] = (arr[0][0] + arr[0][1]) % 9901
    arr[0][1] = (arr[0][0] + temp) % 9901
    i += 1

print(((2 * arr[0][0]) + arr[0][1]) % 9901)
