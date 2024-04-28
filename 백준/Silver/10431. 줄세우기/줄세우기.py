import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    result = 0
    arr = list(map(int, input().split()))
    # print(arr)
    for i in range(2, 21):
        for j in range(i, 1, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                result += 1
        # print(*arr)
        # print(result)
    print(arr[0], result)