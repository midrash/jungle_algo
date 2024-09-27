import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().strip()))

result = 0
for i in arr:
    result += i

print(result)