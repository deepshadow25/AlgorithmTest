def solution(n, words):
    p = [words[0][0]]
    for idx, word in enumerate(words):
        if word not in p and p[-1][-1] == word[0]:
            p.append(word)
            #print(p)
        else:
            return [idx%n+1, (idx//n)+1]
    return [0,0]