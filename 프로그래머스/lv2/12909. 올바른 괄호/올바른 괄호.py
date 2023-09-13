def solution(s):
    num = 0

    for i, j in enumerate(s):
        if i == 0 and j == ')':
            return False
        if i == len(s)-1 and j == '(':
            return False

    for i in range(len(s)):
        if s[i] == '(':
            num += 1
        if s[i] == ')':
            num -= 1
            if num < 0:
                return False

    print(num)
            
    if num == 0:
        return True
    else:
        return False