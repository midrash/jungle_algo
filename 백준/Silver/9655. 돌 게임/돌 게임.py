import sys

input = sys.stdin.readline

N = int(input().strip())

if N % 3 == 0:
    if (int((N / 3)) % 2) == 0:
        print("CY")
    else:
        print("SK")
elif N % 3 == 1:
    if (int((N / 3)) % 2) == 0:
        print("SK")
    else:
        print("CY")
else:
    if (int((N / 3)) % 2) == 0:
        print("CY")
    else:
        print("SK")
