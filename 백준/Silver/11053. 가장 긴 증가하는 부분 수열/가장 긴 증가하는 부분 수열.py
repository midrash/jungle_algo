import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
suyol = [1] * (N)
# print(arr)
# print(suyol)

max_ = 1
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            suyol[i] = max(suyol[i], suyol[j] + 1)
            if max_ < suyol[i]:
                max_ = suyol[i]
# print(suyol)
print(max_)