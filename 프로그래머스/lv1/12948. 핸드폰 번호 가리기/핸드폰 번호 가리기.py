def solution(phone_number):
    return phone_number[:-4].replace(phone_number[:-4],'*'*len(phone_number[:-4])) + phone_number[-4:]