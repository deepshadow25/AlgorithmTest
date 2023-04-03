def solution(n, k):
    num_base = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        num_base += str(mod)
        
    num = num_base[::-1]
    num = num.split('0')
    print(num)
    
    answer = 0
    for i in num:
        if len(i) == 0:
            continue
        if int(i) < 2:
            continue
        prime = True
        for j in range(2, int(int(i)**0.5)+1):
            if int(i) % j == 0:
                prime=False
                break
        if prime:
            answer+=1
    return answer