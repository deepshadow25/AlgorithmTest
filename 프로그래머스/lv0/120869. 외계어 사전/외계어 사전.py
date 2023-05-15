def solution(spell, dic):
    for i in dic:
        if set(spell).issubset(set(i)):
            return 1
    return 2