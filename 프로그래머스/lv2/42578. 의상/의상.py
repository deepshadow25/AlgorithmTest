def solution(clothes):
    answer = 1
    fashion = {part:[] for _,part in clothes}
    for cloth, part in clothes:
        fashion[part].append(cloth)
    for v in fashion.values():
        answer *= (len(v) + 1)
    return answer - 1