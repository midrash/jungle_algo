answer = -1
def solution(k, dungeons):
    global answer
    visit = [False]*len(dungeons)
    dfs(k,0,dungeons,visit)
    return answer

def dfs(k,cnt,dungeons,visit):
    global answer
    if cnt>answer:
         answer = cnt
    for i in range(len(dungeons)):
        if not visit[i] and k >= dungeons[i][0]:
            visit[i]= True
            dfs(k-dungeons[i][1], cnt+1,dungeons,visit)
            visit[i]= False
