import sys

input = sys.stdin.readline

V, E = map(int, input().split())

mst = []
parent = [i for i in range(V + 1)]

for _ in range(E):
    a, b, cost = map(int, input().split())
    mst.append((a, b, cost))

mst.sort(key=lambda x: x[2])
# print(*mst)
# print(parent)
result = 0


def getParent(x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in mst:
    if getParent(i[0]) != getParent(i[1]):
        union_parent(i[0], i[1])
        result += i[2]
print(result)
