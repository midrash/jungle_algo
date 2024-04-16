import sys
from heapq import heappop, heappush

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
leftQue = []
rightQue = []
for i in range(1, N + 1):
    a = int(input())
    # print(f"i:{i}")
    if len(leftQue) == len(rightQue):
        heappush(leftQue, -a)
    else:
        heappush(rightQue, a)

    if rightQue and -leftQue[0] > rightQue[0]:
        lNum = -heappop(leftQue)
        rNum = heappop(rightQue)
        heappush(leftQue, -rNum)
        heappush(rightQue, lNum)
    print(-leftQue[0])
