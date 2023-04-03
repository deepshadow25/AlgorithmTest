from datetime import datetime
print(datetime.now())

answer = 0
n = 0
visited = []

def df(k, count, dungeons):
    global answer
    if count > answer:
        answer = count
        
    for i in range(n): 
        if k >= dungeons[i][0] and visited[i]==0:
            visited[i] = 1
            df(k-dungeons[i][1], count+1, dungeons)
            visited[i] = 0

def solution(k, dungeons):
    global n, visited
    n = len(dungeons)
    visited = [0] * n
    df(k, 0, dungeons)
    return answer