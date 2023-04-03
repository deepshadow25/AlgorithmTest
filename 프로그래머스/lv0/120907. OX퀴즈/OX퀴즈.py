def solution(quiz):
    answer = []
    
    for i in quiz:
        if i.split()[1] == '+':
            if (int(i.split()[0]) + int(i.split()[2])) == int(i.split()[-1]):
                answer.append("O")
            else: 
                answer.append('X')
        if i.split()[1] == "-":
            if (int(i.split()[0]) - int(i.split()[2])) == int(i.split()[-1]): 
                answer.append("O")
            else: 
                answer.append("X")
    return answer