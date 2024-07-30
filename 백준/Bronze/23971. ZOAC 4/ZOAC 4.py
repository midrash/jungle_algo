import sys

input = sys.stdin.readline

# A, B = list(map(int, input().split()))
H, W, N, M = map(int, input().split())
# print(H, W, N, M)

if H % (N + 1) > 0:
    newN = int(H / (N + 1)) + 1
else:
    newN = int(H / (N + 1))
if W % (M + 1) > 0:
    newM = int(W / (M + 1)) + 1
else:
    newM = int(W / (M + 1))
print(newN * newM)