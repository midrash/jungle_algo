import sys

input = sys.stdin.readline
N = int(input())
# print(N)
inoutboard = list(map(int, input().strip()))
# print(inoutboard)
edgeboard = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0


def drawboard():
    for i in range(N + 1):
        print(edgeboard[i])


for _ in range(N - 1):
    l, r = map(int, input().split())
    edgeboard[l].append(r)
    edgeboard[r].append(l)

# drawboard()


def dfs(s):
    global cnt
    for i in edgeboard[s]:
        if visited[i] == False:
            if inoutboard[i - 1] == 1:
                # print(visited)
                # print(f"{i}번 도착 산책끝")
                cnt += 1
                continue
            else:
                visited[i] = True
                dfs(i)
                visited[i] = False


for i in range(1, N + 1):
    if inoutboard[i - 1] == 1:
        visited = [False] * (N + 1)
        # print(f"{i}번 들어간다")
        visited[i] = True
        dfs(i)

print(cnt)
