import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

M, N, H = map(int, input().split())
direct = [(0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]


def draw():
    for i in range(H):
        for j in range(N):
            print(box[i][j])
    for i in range(H):
        for j in range(N):
            print(visited[i][j])


# draw()


def bfs():
    max = 0
    que = deque()
    # 익은 토마토 위치 찾기
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    visited[i][j][k] = True
                    que.append((i, j, k, 0))
                elif box[i][j][k] == -1:
                    visited[i][j][k] = True
    while que:
        nz, ny, nx, nc = que.popleft()
        if max < nc:
            max = nc
        # print(
        #     f"이번 토마토 좌표 {nz}{ny}{nx}, 익는데 걸린 시간:{nc} 이때까치 최대 시간 :{max}, 방문여부 {visited[nz][ny][nx]}"
        # )
        for pz, py, px in direct:
            tz = nz + pz
            ty = ny + py
            tx = nx + px
            if (
                tz >= 0
                and tz < H
                and ty >= 0
                and ty < N
                and tx >= 0
                and tx < M
                and visited[tz][ty][tx] == False
                and box[tz][ty][tx] == 0
            ):
                visited[tz][ty][tx] = True
                que.append((tz, ty, tx, nc + 1))
    # 덜익은 토마토 확인
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == False:
                    # print(f"안익은 토마토 좌표 {i}{j}{k}")
                    return -1
    return max


print(bfs())
