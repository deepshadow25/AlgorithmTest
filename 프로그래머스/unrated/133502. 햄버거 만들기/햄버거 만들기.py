def solution(ingredient):
    answer = 0
    i = 0
    
    while i <= len(ingredient):
        if ingredient[i:i+4] == [1,2,3,1]:
            answer += 1
            del (ingredient[i:i+4])
            i = i - 3
        i += 1
        
    return answer