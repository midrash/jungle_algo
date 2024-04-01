import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
syms = list(map(int, input().split()))
min = sys.maxsize
max = sys.maxsize * (-1)


def calculate(a, b, sysm):
    # print(f" a: {a}, b: {b}, sysm: {syms}")
    if sysm == 0:
        return a + b
    elif sysm == 1:
        return a - b
    elif sysm == 2:
        return a * b
    else:
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            return (abs(a) // abs(b)) * (-1)
        else:
            return abs(a) // abs(b)


def dfs(now, sum, syms):
    global max, min
    # print(
    #     f"이번 숫자는 {numbers[now]}야, 이때까지 합은 {sum}이고, 남은 기호는 카운터는 +:{syms[0]}, -:{syms[1]}, *:{syms[2]}, %:{syms[3]},야"
    # )
    for i in range(4):
        if syms[i] > 0:
            newsum = calculate(sum, numbers[now], i)
            if now + 1 == N:
                if newsum > max:
                    max = newsum
                if newsum < min:
                    min = newsum
                continue
            syms[i] -= 1
            dfs(now + 1, newsum, syms)
            syms[i] += 1


dfs(1, numbers[0], syms)
# print(f"최대값 :{max}, 최소값:{min}")
print(max, min)
