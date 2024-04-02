import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
tree = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    tree[a].append((c, b))

start, goal = map(int, input().split())

cost = [sys.maxsize] * (N + 1)
que = []
cost[start] = 0
heapq.heappush(que, (0, start))
# print(f"큐 업데이트 : {que}")

while que:
    nowCost, startNode = heapq.heappop(que)
    if cost[startNode] < nowCost:
        continue
    # print(f"출발지: {node}")
    for toCost, toNode in tree[startNode]:
        # print(f"확인 장소 : {toNode}, 비용 {toCost}")
        # print(f"기존 비용 : {cost[toNode]}, 새 비용 {cost[node] + toCost}")
        if cost[toNode] > nowCost + toCost:
            cost[toNode] = nowCost + toCost
            # print(f"비용 업데이트 : {cost}")
            heapq.heappush(que, (nowCost + toCost, toNode))
        # print(f"큐 업데이트 : {que}")

print(f"{cost[goal]}")


