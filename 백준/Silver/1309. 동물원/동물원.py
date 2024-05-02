import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
left = 1
right = 1
i = 1
while i < N:
    temp = left
    left = (left + right)%9901
    right = (left + temp)%9901
    i += 1

print((2 * (left) + right) % 9901)
