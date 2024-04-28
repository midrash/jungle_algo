import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [0] * 10001

for i in range(n):
    arr[int(input())] += 1

for i in range(1, 10001):
    j = arr[i]
    for _ in range(j):
        print(i)
