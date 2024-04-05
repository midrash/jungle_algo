import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
# print(n)

fibo = [0, 1]

# for i in range(2, n + 1):
#     fibo.append(fibo[i - 1] + fibo[i - 2])
# print(fibo[n])

fibonachi = [-1] * (n + 1)


def fibo(n):
    if fibonachi[n] >= 0:
        return fibonachi[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonachi[n] = fibo(n - 1) + fibo(n - 2)
        return fibonachi[n]


print(fibo(n))
