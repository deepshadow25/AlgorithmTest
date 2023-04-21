from collections import deque

def solution(n, roads, sources, destination):
    visited = [-1]*(n+1)
    graph = [[] for _ in range(n+1)]
    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start)        
    
    q = deque([destination])
    visited[destination] = 0
    while q:
        now = q.popleft()        
        for node in graph[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                q.append(node)
                
    return [visited[i] for i in sources]
