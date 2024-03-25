import sys
A, B, C = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))

def jegob(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (jegob(a, b // 2, c) ** 2) % c
    else:
        return (jegob(a, b // 2, c) ** 2) * a % c


print(jegob(A, B, C))
