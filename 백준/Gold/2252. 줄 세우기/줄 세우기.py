import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)
tree = [[] for _ in range(N + 1)]
edge = [0] * (N + 1)
result = []


def draw():
    for i in range(N + 1):
        print(tree[i])
    print(edge)


for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    edge[b] += 1

# draw()


def topology():
    # 큐 선언
    que = deque()
    # 들어오는 간선의 개수가 0인 노드 큐에 추가
    for i in range(1, N + 1):
        if edge[i] == 0:
            que.append(i)
    # print(que)
    while que:
        node = que.popleft()
        result.append(node)
        # print(f"큐에서 이거나옴: {node}, result :{result}")
        for i in tree[node]:
            edge[i] -= 1
            if edge[i] == 0:
                que.append(i)
                # print(f"que에 새거들어옴: {i}, que :{que}")


topology()
print(*result)
