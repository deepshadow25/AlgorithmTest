def solution(s):
    answer = []
    li = s.split(' ')
    for i in li:
        for j in range(len(i)):
            if j%2==0:
                answer.append(i[j].upper())
            if j%2!=0:
                answer.append(i[j].lower())
    for i in range(len(s)):
        if s[i] == ' ':
            answer.insert(i, ' ')
    result = ''
    for i in range(len(answer)):
        result += answer[i]
    return result