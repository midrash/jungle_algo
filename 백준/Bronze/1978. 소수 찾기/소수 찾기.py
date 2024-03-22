N = int(input())
arr = list(map(int, input().split()))
result = 0
# print(arr)
for i in arr:
    if i == 2:
        result = result + 1
        continue
    for j in range(2, i):
        if i == 2:
            result = result + 1
            continue
        if i % j == 0:
            break
        if j + 1 == i:
            result = result + 1
print(result)
