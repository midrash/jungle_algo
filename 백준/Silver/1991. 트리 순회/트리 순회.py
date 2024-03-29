import sys

input = sys.stdin.readline
N = int(input())
tree = {}
for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root] = (left, right)


# print(N)
# for i in tree:
#     print(i, tree[i])


def preOrder(root):
    print(root, end="")
    if tree[root][0] != ".":
        preOrder(tree[root][0])
    if tree[root][1] != ".":
        preOrder(tree[root][1])


def inOrder(root):
    if tree[root][0] != ".":
        inOrder(tree[root][0])
    print(root, end="")
    if tree[root][1] != ".":
        inOrder(tree[root][1])


def postOrder(root):
    if tree[root][0] != ".":
        postOrder(tree[root][0])
    if tree[root][1] != ".":
        postOrder(tree[root][1])
    print(root, end="")


preOrder("A")
print()
inOrder("A")
print()
postOrder("A")
