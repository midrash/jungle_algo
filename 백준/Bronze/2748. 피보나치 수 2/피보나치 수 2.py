import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
# print(n)

fibo = [0, 1]

for i in range(2, n + 1):
    fibo.append(fibo[i - 1] + fibo[i - 2])
print(fibo[n])
