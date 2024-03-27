import sys
from collections import deque

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
top = deque()
result = []
# print(arr)

for i in range(1, len(arr) + 1):
    arr[i - 1] = (i, arr[i - 1])

# print(arr)

for i in range(1, len(arr) + 1):
    if len(top) == 0:
        print(f"0 ", end="")
        top.append(arr[i - 1])
    else:
        while len(top) > 0:
            temp = top.pop()
            # print(f"스택{temp[1]} ,탑{arr[i - 1][1]} ")
            if temp[1] > arr[i - 1][1]:
                print(f"{temp[0]} ", end="")
                top.append(temp)
                top.append((arr[i - 1]))
                # print(f"크다 {top} ")
                break
            if len(top) == 0:
                print(f"0 ", end="")
                top.append((arr[i - 1]))
                # print(f"작다 {top} ")
                break