def solution(num, k):
    num = str(num)
    result = []
    for i in range(len(num)):
        if num[i] == str(k):
            result.append(num[i])
            break
        if num[i] != str(k):
            result.append(0)
    if result[-1] != str(k):
        return -1
    return len(result)