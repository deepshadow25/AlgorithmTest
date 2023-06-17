def solution(s):
    return " ".join([w[0].upper() + w[1:].lower() if w else w for w in s.split(' ')])
    
    #s = s.split(' ')
    #answer = ''
    #for w in s:
    #    if w:
    #        answer += w[0].upper() + w[1:].lower()
    #    else:
    #        answer += w
    #return answer