import sys
import heapq

#sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
classes = [list(map(int,input().split())) for _ in range(N)]

classes.sort(key=lambda x :x[1])

room =[]
heapq.heappush(room,classes[0][2])

for i in range(1,N):
    if classes[i][1] < room[0]:
        heapq.heappush(room,classes[i][2])
    else:
        heapq.heappop(room)
        heapq.heappush(room,classes[i][2])

print(len(room))