import sys
# sys.stdin = open("input.txt","r")
input = sys.stdin.readline
num = input().strip()
arr = list(map(str,num))
# print(arr[1])
result = 0
if len(arr)==1 :
    result = arr[0]
elif arr[1]=="x":
    result = int(num,16)
elif arr[0]=="0":
    result = int(num,8)
else:
    result = int(num,10)
    
print(result)