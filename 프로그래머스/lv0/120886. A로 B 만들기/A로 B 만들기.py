def solution(before, after):
    return [1 if sorted(' '.join(before).split(' ')) == sorted(' '.join(after).split(' ')) else 0][0]