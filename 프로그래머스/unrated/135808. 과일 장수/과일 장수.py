def solution(k, m, score):
    score = sorted(score, reverse=True)
    return m*sum([score[i+m-1] for i in range(0, len(score), m) if i+m<=len(score)])