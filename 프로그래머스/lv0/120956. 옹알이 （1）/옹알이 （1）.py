def solution(babbling):
    baby = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for i in babbling:
        i = i.replace('aya', '1')
        i = i.replace('ye', '2')
        i = i.replace('woo', '3')
        i = i.replace('ma', '4')
        if i.isdigit()==True:
            answer += 1
    return answer