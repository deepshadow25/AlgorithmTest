a, b = map(int, input().strip().split(' '))
solution = lambda a, b:('*'*a+'\n')*b
print(solution(a,b))