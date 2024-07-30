import sys

input = sys.stdin.readline

M = input().strip()
arr = set()
for i in range(int(M)):
    cmd = list(input().split())
    if len(cmd) > 1:
        cmd[1] = int(cmd[1])
        if cmd[0] == "add":
            arr.add(cmd[1])
        elif cmd[0] == "remove":
            arr.discard(cmd[1])
        elif cmd[0] == "check":
            if cmd[1] in arr:
                print(1)
            else:
                print(0)
        elif cmd[0] == "toggle":
            if cmd[1] in arr:
                arr.discard(cmd[1])
            else:
                arr.add(cmd[1])
    else:
        # print(cmd[0])
        if cmd[0] == "all":
            arr = set(list(range(1, 21)))
        elif cmd[0] == "empty":
            arr = set()
