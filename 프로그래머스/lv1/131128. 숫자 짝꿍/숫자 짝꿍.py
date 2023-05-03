from collections import Counter
def solution(X, Y):
    result = sorted(list( 
        (Counter(int(i) for i in X )&Counter(int(i) for i in Y)).elements()
    ), reverse=True)
    if result == []:    
        return "-1"
    elif result[0] == 0:  
        return "0"
    else:
        return ''.join((str(i) for i in result))