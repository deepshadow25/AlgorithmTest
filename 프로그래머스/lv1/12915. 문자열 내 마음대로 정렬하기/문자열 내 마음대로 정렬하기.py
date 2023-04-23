def solution(strings, n):
    for i in range(len(strings)-1):
        for j in range(i, len(strings)):
            if strings[i][n] > strings[j][n]:
                temp = strings[i]
                strings[i], strings[j] = strings[j], temp
            elif strings[i][n] == strings[j][n]:
                if strings[i] > strings[j]:
                    temp = strings[i]
                    strings[i], strings[j] = strings[j], temp
                else:
                    continue
            else:
                continue
    return strings