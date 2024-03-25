import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(arr)

while start <= end:
    wood_sum = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            wood_sum += i - mid
    if wood_sum >=M:
        start = mid+1
    else:
        end = mid-1

print(end)
