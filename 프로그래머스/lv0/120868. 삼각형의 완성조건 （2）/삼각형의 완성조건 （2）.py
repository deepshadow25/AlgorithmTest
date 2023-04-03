def solution(sides):
    sides = sorted(sides)
    return len(range(sides[1]-sides[0],sides[1])) + len(range(sides[1]+1, sides[1]+sides[0]))
        