def solution(s):
    alpha_to_digit = {'zero':'0','one':'1','two':'2','three':'3',
                      'four':'4','five':'5','six':'6',
                      'seven':'7','eight':'8','nine':'9'}
    for k, v in alpha_to_digit.items():
        s = v.join(s.split(k))
    return int(s)
