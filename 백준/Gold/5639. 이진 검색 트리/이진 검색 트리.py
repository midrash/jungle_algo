import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
# class Node:
#     def __init__(self,key,left,right) -> None:
#         self.key = key
#         self.left = left
#         self.right = right
# class Bst:
#     def __init__(self) -> None:
#         self.root= None
#     def add(self,key):
#         if self.root == None:


# tree = Bst()

tree = {}
arr = []
ip = input()
while ip != "":
    arr.append(int(ip))
    ip = input()
# print(arr)

def postorder(arr):
    if len(arr) == 0:
        return
    root = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if root > arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    # print(left)
    if len(left) != 0:
        postorder(left)
    # print(right)
    if len(right) != 0:
        postorder(right)
    print(root)


postorder(arr)
