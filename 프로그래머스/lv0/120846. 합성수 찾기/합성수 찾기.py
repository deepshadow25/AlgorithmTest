def solution(n):
    return len(set([i for i in range(1, n+1) if i%2==0 and i>2]
    +[i for i in range(1, n+1) if i%3==0 and i>3]
    +[i for i in range(1, n+1) if i%5 ==0 and i>5]
    +[i for i in range(1, n+1) if i%7==0 and i>7]))