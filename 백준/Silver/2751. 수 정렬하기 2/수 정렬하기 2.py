import sys

# sys.stdin = open("input.txt", "r")
# N = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(N)]

N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]


arr.sort()

for i in arr:
    print(i)
