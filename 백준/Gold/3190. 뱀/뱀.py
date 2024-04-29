import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
# board = [[0]*N+1 for _ in range(N+1) ]
apple_cnt = int(input())
apples = []
for _ in range(apple_cnt):
    y, x = map(int, input().split())
    apples.append([y, x, 1])
    # board[y][x]= 1
move_cnt = int(input())
moves = []
last_move_cnt = 0
for _ in range(move_cnt):
    t, d = map(str, input().split())
    moves.append((int(t), d))
    if int(t) > last_move_cnt:
        last_move_cnt = int(t)
move_cnt = 0
# print(apples)
# print(moves)

snake = deque()
survive_time = 0
snake.append((1, 1, 0))


def checkbite(y, x):
    for i in range(len(snake)):
        if y == snake[i][0] and x == snake[i][1]:
            return True
    return False


def checkapple(y, x):
    for i in range(len(apples)):
        if y == apples[i][0] and x == apples[i][1] and apples[i][2] == 1:
            apples[i][2] = 0
            return True
    return False


def checkdirection(t):
    global move_cnt
    # print(f"move_cnt:{move_cnt}")
    if last_move_cnt >= t and moves[move_cnt][0] == t:
        move_cnt += 1
        return moves[move_cnt - 1][1]
    return False


while True:
    survive_time += 1
    # print(f"현재 시간 : {survive_time}")
    head_y, head_x, dir = snake.pop()
    snake.append((head_y, head_x, dir))
    # print(f"뱀 : {snake}")
    next_head_y = head_y + direction[dir][0]
    next_head_x = head_x + direction[dir][1]
    # print(f"다음 머리 위치 : {next_head_y},{next_head_x}")
    if (
        next_head_y <= 0
        or next_head_y > N
        or next_head_x <= 0
        or next_head_x > N
        or checkbite(next_head_y, next_head_x)
    ):
        # print(f"머리 뜌땨")
        break
    else:
        # survive_time += 1
        if checkapple(next_head_y, next_head_x) == False:
            # print("사과 없음")
            snake.popleft()
        move = checkdirection(survive_time)
        # print(f"move체크 결과:{move}")
        if move != False:
            if move == "D":
                snake.append((next_head_y, next_head_x, (dir + 5) % 4))
            else:
                snake.append((next_head_y, next_head_x, (dir + 3) % 4))
        else:
            snake.append((next_head_y, next_head_x, dir))

print(survive_time)
