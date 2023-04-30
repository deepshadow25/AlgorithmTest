def solution(want, number, discount):
    answer, total = 0, []
    
    for pd, n in zip(want, number):
        total.extend([pd]*n)
        total.sort()
    
    for idx, pd in enumerate(discount[:-len(total)+1]):
        if pd in total and total == sorted(discount[idx:len(total)+idx]):
            answer += 1
           
    return answer