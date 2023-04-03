def solution(age):
    age = str(age)
    aget = age.maketrans('0123456789','abcdefghij')
    age = age.translate(aget)
    return age