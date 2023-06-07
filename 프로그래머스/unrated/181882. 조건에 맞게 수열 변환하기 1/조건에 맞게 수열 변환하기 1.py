def solution(arr):
    #answer = []
    return [i//2 if (i%2==0 and i>=50) 
            else 2*i if (i%2!=0 and i<50) 
            else i 
            for i in arr]
    #for i in arr:
    #    if i%2==0 and i>=50:
    #        answer.append(i//2)
    #    elif i%2!=0 and i<50:
    #        answer.append(2*i)
    #    else:
    #       answer.append(i)
    #return answer