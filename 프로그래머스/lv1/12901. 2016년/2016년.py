def solution(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a == 1:
        return week[(b-1)%7]
    else:
        return week[(sum(month[:a-1])+b-1)%7]