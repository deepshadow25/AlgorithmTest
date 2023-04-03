def solution(p):
    if p=="":
        return ""
    
    def braket(p):
        if p[0] == ')' or p[len(p)-1] == "(":
            return False
        left_cnt = 0
        right_cnt = 0
        for cnt in p:
            if cnt == '(':
                left_cnt += 1
            if cnt == ')':
                right_cnt += 1
            if left_cnt < right_cnt:
                return False
        if left_cnt != right_cnt:
            return False
        return True
    
    def fix_state(p):
        if not p:
            return p
        u = ''
        v = ''
        left_cnt = 0
        right_cnt = 0
        for i in p:
            u += i
            if i == '(':
                left_cnt += 1
            if i == ')':
                right_cnt += 1
            if left_cnt == right_cnt:
                break
        v = p[len(u):]
        
        if braket(u):
            return u + fix_state(v)
        else:
            tmp = '('
            tmp += fix_state(v)
            tmp += ')'
            for s in u[1:len(u)-1]:
                if s == "(":
                    tmp += ")"
                else:
                    tmp += "("
            return tmp

    status = braket(p)

    if status == True:
        return p
    else:
        return fix_state(p)
    return ""   