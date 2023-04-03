def intersec(A, B):
    n = 0  
    for x in set(A):
        if x in B:
            n += min(A.count(x), B.count(x))
    return n

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    A = [str1[i:i+2] for i in range(len(str1)-1)
        if str1[i:i+2].isalpha() == True and len(str1[i:i+2])==2]
    B = [str2[j:j+2] for j in range(len(str2)-1)
        if str2[j:j+2].isalpha() == True and len(str2[j:j+2])==2]
    
    inter = 0
    if len(A) < len(B):
        inter = intersec(A, B)
    else:
        inter = intersec(B, A)
            
    if (len(A)+len(B)-inter) == 0:
        return 65536
    else:
        return int(inter / (len(A)+len(B)-inter) * 65536)