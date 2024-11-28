import sys

input = sys.stdin.readline

N = int(input())
dp=[1]*N
arr =[]
for i in range(N):
    arr.append(int(input()))
for i in range(N):
    max_=0
    for j in range(i):
        if arr[i]>arr[j] and dp[j]>max_:
            max_= dp[j]
    dp[i]= max_+1

print(N-max(dp))