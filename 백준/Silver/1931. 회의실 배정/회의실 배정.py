import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
min = sys.maxsize
max = -(sys.maxsize)
time = []
for i in range(N):
    a, b = map(int, input().split())
    time.append((a, b))

time.sort(key=lambda x: (x[1], x[0]))
# print()
visited = [0] * (max + 1)
# print(time)

# for i in range(N):
#     print(time[i])


usecnt = 0
endtime = 0
# print(f"start :{start}")
# print()
for start, end in time:
    # print(f"시작시간:{start}, 종료시간:{end},  ")
    if start >= endtime:
        endtime = end
        usecnt += 1

print(usecnt)