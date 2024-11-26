import sys

input = sys.stdin.readline

N = int(input())
dp= [0]*N
arr = list(map(int,input().split()))
dp[0]=1
for i in range(N):
    max_=0
    for j in range(i):
        if arr[j]<arr[i] and max_<dp[j]:
            max_= max_+1
    dp[i]= max_+1
print(max(dp))