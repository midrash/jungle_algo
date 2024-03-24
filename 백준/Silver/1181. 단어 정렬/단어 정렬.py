N = int(input())
# arr = [sys.stdin.readline() for _ in range(N)]
arr = [input() for _ in range(N)]

arr = list(set(arr))


# def buble(a):
#     n = len(a)
#     while stp < n - 1:
#         change = 0
#         last = n - 1
#         for j in range(n - 1, stp, -1):
#             if len(a[j - 1]) > len(a[j]):
#                 a[j - 1], a[j] = a[j], a[j - 1]
#                 change += 1
#                 last = j
#             elif len(a[j - 1]) == len(a[j]):
#                 for k in range(len(a[j - 1])):
#                     if ord(a[j - 1][k]) > ord(a[j][k]):
#                         a[j - 1], a[j] = a[j], a[j - 1]
#                         change += 1
#                         last = j
#                         break

#         stp = last
#         if change == 0:
#             break


# buble(arr)

arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)
