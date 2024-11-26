import sys
from collections import deque

dq = deque()
input= sys.stdin.readline

N,M,V = map(int,input().split())
map_ = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    map_[a].append(b)
    map_[b].append(a)
    
for i in range(1,len(map_)):
    map_[i].sort()
    
result=[]
visited = [False]*(N+1)

def print_result(result):
    for i in range(len(result)):
        print(result[i],end=" ")
    print()

def dfs(v):
    visited[v]= True
    result.append(v)
    for i in map_[v]:
        if not visited[i]:
            dfs(i)

dfs(V)
print_result(result)

result=[]
visited = [False]*(N+1)
def bfs(v):
    dq.append(v)
    visited[v]=True
    result.append(v)
    while len(dq)>0:
        num = dq.popleft()
        for i in map_[num]:
            if not visited[i]:
                dq.append(i)
                visited[i]=True
                result.append(i)
bfs(V)
print_result(result)

