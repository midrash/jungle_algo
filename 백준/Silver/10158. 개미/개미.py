import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

x, y = map(int, input().split())
ant_x, ant_y = map(int, input().split())
t = int(input())

t_x = (
    int((t + ant_x) % x)
    if ((int((t + ant_x) / x)) % 2 == 0)
    else x - int((t + ant_x) % x)
)
t_y = (
    int((t + ant_y) % y)
    if ((int((t + ant_y) / y)) % 2 == 0)
    else y - int((t + ant_y) % y)
)

print(f"{t_x} {t_y}")
