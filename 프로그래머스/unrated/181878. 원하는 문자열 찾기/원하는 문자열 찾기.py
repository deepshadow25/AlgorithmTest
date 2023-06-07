def solution(myString, pat):
    myString, pat = myString.lower(), pat.lower()
    return 1 if pat in myString else 0