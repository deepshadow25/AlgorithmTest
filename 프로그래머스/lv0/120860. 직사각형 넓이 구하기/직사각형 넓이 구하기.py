def solution(dots):
    h, v = [], []
    for x, y in dots:
        h.append(x)
        v.append(y)
    return (max(h)-min(h)) * (max(v)-min(v))