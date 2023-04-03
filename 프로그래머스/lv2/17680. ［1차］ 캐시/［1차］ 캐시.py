def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else:
            cache.append(c)
            if len(cache)>cacheSize:
                cache.pop(0)
            answer += 5
    return answer