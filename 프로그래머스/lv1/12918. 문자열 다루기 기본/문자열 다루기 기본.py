def solution(s):
    try:
        if not (len(s)==4 or len(s)==6):
            return False
        int(s)
    except:
        return False
    return True