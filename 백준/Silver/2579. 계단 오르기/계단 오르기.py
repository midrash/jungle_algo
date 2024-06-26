import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [0]
for i in range(N):
    arr.append(int(input()))
# print(arr)
dp = [0] * (N + 1)
if N == 1:
    dp[1] = arr[1]
elif N == 2:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
elif N > 2:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i] + arr[i - 1])
# print(dp)
print(dp[N])