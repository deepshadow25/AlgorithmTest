def solution(q, r, code):
    return ''.join([letter for idx, letter in enumerate(code) if idx % q == r])