import sys
sys.setrecursionlimit(1000000)

def solution(elements):
    answer = set()
    n = len(elements)
    
    def dfs(idx, rest, count):
        if count > n:
            return
    
        rest += elements[idx]
        answer.add(rest)
        dfs((idx+1)%n, rest, count+1)
    
    for i in range(n):
        dfs(i, 0, 1)
    
    return len(answer)