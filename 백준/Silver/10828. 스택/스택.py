import sys

A = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
s_list = []
for _ in range(A):
    command = list(sys.stdin.readline().split())
    # print(command)
    if command[0] == "push":
        s_list.append(command[1])
    elif command[0] == "top":
        if len(s_list) > 0:
            print(s_list[len(s_list) - 1])
        else:
            print(-1)
    elif command[0] == "size":
        print(len(s_list))
    elif command[0] == "empty":
        if len(s_list) > 0:
            print(0)
        else:
            print(1)
    elif command[0] == "pop":
        if len(s_list) > 0:
            print(s_list[len(s_list) - 1])
            s_list.pop()
        else:
            print(-1)
