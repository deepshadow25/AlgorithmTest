import sys
sys.setrecursionlimit(10000)

def solution(s):

    global cnt
    cnt = 1

    def recur(s):
        tmp = s[0]
        x, y = 1, 0
        global cnt

        for idx, val in enumerate(s[1:]):

            if x == y:
                cnt += 1
                return recur(s[idx+1:])

            if idx == len(s)-1:
                cnt += 1
                break

            if val == tmp:
                x += 1
            else: 
                y += 1
    recur(s)
    return cnt