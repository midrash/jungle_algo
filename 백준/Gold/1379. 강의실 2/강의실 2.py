import sys

from heapq import heappush, heappop

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
lesson = []
que = []
classroom = [0] * (N + 1)
useCalssRoom = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    lesson.append((c, b, a))
lesson.sort(key=lambda x: x[1])

# for i in range(len(lesson)):
#     print(lesson[i])

for end, start, index in lesson:
    # print(f"idx:{index}, start:{start}, end:{end}")
    if que and que[0][0] <= start:
        lessonUseRoom = que[0][3]
        heappop(que)
        classroom[index] = lessonUseRoom
        heappush(que, (end, start, index, lessonUseRoom))
    else:
        useCalssRoom += 1
        classroom[index] = useCalssRoom
        heappush(que, (end, start, index, useCalssRoom))
    # print(f"que:{que}")
    # print(f"classroom:{classroom}")
while que:
    index = que[0][2]
    lessonUseRoom = que[0][3]
    # print(f"index:{index}, useClassRoom:{lessonUseRoom}")
    classroom[index] = lessonUseRoom
    heappop(que)
# print(f"que:{que}")
# print(f"classroom:{classroom}")

print(useCalssRoom)
for i in range(1, N+1):
    print(classroom[i])
