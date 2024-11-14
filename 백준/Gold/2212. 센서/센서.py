import sys

# sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = sorted(set(list(map(int,input().split()))))

n_arr = []
for i in range(1,len(arr)):
    n= arr[i]- arr[i-1]
    if n-1>0:
        n_arr.append(n)
n_arr= sorted(n_arr,reverse=True)

for _ in range(len(n_arr)-(K-1)):
    n_arr.pop()

print(arr[len(arr)-1]-arr[0]-sum(n_arr))