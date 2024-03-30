import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
# print(N, M, K, X)
city_edge = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
visited[0] = True
result = []


def drawcity():
    for i in range(N + 1):
        print(city_edge[i])
    print(visited)


for i in range(M):
    a, b = map(int, input().split())
    # print(a, b)
    city_edge[a].append(b)

# drawcity()


def bfs(n, cnt):
    que = deque()
    visited[n] = True
    que.append((n, cnt))
    while len(que) > 0:
        now = que.popleft()
        if now[1] > K:
            # print(f"여기서부턴 의미없다")
            return
        # print(f"이번도시야 :{now[0]}, cnt :{now[1]}")
        for i in city_edge[now[0]]:
            # print(f"체크중인도시는  :{i}")
            if visited[i] == False:
                # print(f"X :{X}, cnt+1 :{now[1] + 1}")
                if now[1] + 1 == K:
                    result.append(i)
                    # print(f"{result} 만큼 들어왔어")
                visited[i] = True
                que.append((i, now[1] + 1))


bfs(X, 0)
if len(result) > 0:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
