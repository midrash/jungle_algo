import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# print(arr)
dp = [1] * N
max_ = 1
for i in range(1, N):
    # print(f"이번 체크 문자:{arr[i]}")
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_:
                max_ = dp[i]
    # print(dp)
print(max_)
