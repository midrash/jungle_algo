import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
dp= [0]*N
dp[0]= arr[0]
for i in range(N):
    max_=0
    for j in range(i):
        if arr[j]<arr[i] and dp[j]>max_:
            max_= dp[j]
    dp[i]= max_+arr[i]
# print(arr)
# print(dp)
print(max(dp))