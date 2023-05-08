def solution(routes):
    answer, n = 0, 0
    routes = sorted(routes, key = lambda x:x[1])
    while n < len(routes):
        if n < len(routes):
            pos = routes[n][1]
        n += 1
        while n < len(routes) and routes[n][0] <= pos and pos <= routes[n][1] :
            n += 1
        answer += 1
    return answer