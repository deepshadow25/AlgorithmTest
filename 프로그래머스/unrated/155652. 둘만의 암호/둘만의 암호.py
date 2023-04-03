alphabet = 'abcdefghijklmnopqrstuvwxyz'

def solution(s, skip, index):
    alpha_skipped = ''
    for char in alphabet:
        if char in list(skip):
            pass
        else:
            alpha_skipped += char
            
    alpha_shift = [alpha_skipped[(i+index)%len(alpha_skipped)] for i in range(len(alpha_skipped))]
    
    answer = ''
    for i in range(len(s)):
        for j in range(len(alpha_skipped)):
            if s[i] == alpha_skipped[j]:
                answer += alpha_shift[j]

    return answer