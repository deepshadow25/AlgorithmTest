def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    result = []
    for people in photo:
        cnt = 0
        for person in people:
            cnt += score.get(person,0)
        result.append(cnt)
    return result