def solution(strArr):
    result = []
    for ind, st in enumerate(strArr):
        if ind%2==0:
            result.append(st.lower())
        else:
            result.append(st.upper())
    return result