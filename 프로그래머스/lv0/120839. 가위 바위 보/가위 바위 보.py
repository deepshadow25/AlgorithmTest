def solution(rsp):
    result = ''
    for i in range(len(rsp)):
        if rsp[i] == '2':
            result += '0'
        if rsp[i] == '0':
            result += '5'
        if rsp[i] == '5':
            result += '2'
    return result