import sys

# sys.setrecursionlimit(10**9)
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = []
dp = [[0] * (N) for _ in range((1 << N))]

for i in range(N):
    board.append(list(map(int, input().split())))


def drawdp():
    for i in range((1 << N)):
        print(dp[i])
    print()


# draw()s
# drawdp()
def dfs(city, visited):
    # print(f"이번도시: {city}, 방문기록: {visited}")
    if visited == ((1 << N) - 1):  # 모두 방문했으면 시작위치로 돌아가는비용 리턴
        if board[city][0]:
            return board[city][0]
        else:
            return sys.maxsize
    if dp[visited][city] != 0:  # 한번 방문한 곳이면 저장된 비용 리턴
        return dp[visited][city]
    dp[visited][city] = sys.maxsize
    for tocity in range(N):
        if board[city][tocity] == 0:
            continue
        if visited & (1 << tocity):
            continue
        dp[visited][city] = min(
            (dp[visited][city]),
            dfs(tocity, (visited | (1 << tocity))) + board[city][tocity],
        )
    return dp[visited][city]


# dfs(0, 1)
# drawdp()
print(dfs(0, 1))