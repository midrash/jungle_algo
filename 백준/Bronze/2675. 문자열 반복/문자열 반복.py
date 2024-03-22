t = int(input())
for i in range(t):
    n, str = input().split()
    n = int(n)
    arr = list(str)
    for j in arr:
        for k in range(n):
            print(j, end="")
    print("")