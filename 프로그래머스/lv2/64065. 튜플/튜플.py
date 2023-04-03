import re
def solution(s):
    dic = {}
    answer = []
    s = re.sub("[^0-9,]",'',s)
    s = s.split(',')  
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    result = sorted(dic.items(),key=lambda x:x[1], reverse=True)
    return [int(i[0]) for i in result]