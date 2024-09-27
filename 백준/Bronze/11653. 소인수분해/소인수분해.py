import sys
input = sys.stdin.readline

N = int(input())
# print(N)
i = 2
while (True):
    if N%i == 0:
        N= int(N/i)
        print(i)
        i = 2
    else:
        i+=1
    if N == 1:
        break