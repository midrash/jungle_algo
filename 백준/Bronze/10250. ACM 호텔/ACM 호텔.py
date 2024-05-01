import sys

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())
for i in range(t):
    result = 0
    h, w, n = map(int, input().split())
    nw = (n // h) + 1 if n % h != 0 else (n // h)
    nh = n % h if n % h != 0 else h
    # print(f"h:{h} ,w:{w} ,n:{n} ,nw:{nw} ,nh:{nh}")
    if nw < 10:
        result = str(nh) + "0" + str(nw)
    else:
        result = str(nh) + str(nw)
    print(result)
