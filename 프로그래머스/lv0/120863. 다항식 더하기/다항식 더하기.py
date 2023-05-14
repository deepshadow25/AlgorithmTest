def solution(polynomial):
    polynomial = polynomial.split()
    xlist = [i for i in polynomial if 'x' in i]
    num = [int(i) for i in polynomial if 'x' not in i and i != '+']
    xans = [int(x[:-1]) if x[0] != 'x' else 1 for x in xlist]
    if sum(xans) != 1 and sum(xans) != 0:
        return f"{sum(xans)}x + {sum(num)}" if sum(num) != 0 else f"{sum(xans)}x"
    elif sum(xans) == 1:
        return f"x + {sum(num)}" if sum(num) != 0 else "x"
    elif sum(xans) == 0:
        return f"{sum(num)}"