str = input()
answer = ''
for i in str:
    if i.isupper() == 1:
        answer += i.lower()
    else:
        answer += i.upper()
print(answer)