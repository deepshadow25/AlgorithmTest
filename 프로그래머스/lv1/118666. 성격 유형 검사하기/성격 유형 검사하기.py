
def solution(survey, choices):
    types = {'A':0,"C":0,'F':0,'J':0,'M':0,'N':0,'R':0,'T':0}
    answer = ''
    
    for i in range(len(choices)):
        left = survey[i][0]
        right = survey[i][1]
        if choices[i] < 4:
            types[left] += 4 - choices[i]
        elif choices[i] > 4:
            types[right] += choices[i] - 4
            
    answer += 'R' if types['R'] >= types['T'] else 'T'
    answer += 'C' if types['C'] >= types['F'] else 'F'
    answer += 'J' if types['J'] >= types['M'] else 'M'
    answer += 'A' if types['A'] >= types['N'] else 'N'
            
    return answer