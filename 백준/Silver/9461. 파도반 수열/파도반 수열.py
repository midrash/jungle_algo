import sys

input = sys.stdin.readline

T = int(input())
arr = [1,1,1,2,2,3,4,5,7,9]

for i in range(10,100):
    arr.append(arr[i-1]+arr[i-5])


for _ in range(T):
    n = int(input())
    print(arr[n-1])