def five(n, k):
    if n==1:
        if k <= 2:
            return k
        else:
            return k-1
        
    div = 5**(n-1)
    one = 4**(n-1)
    iloc = k//div
    
    if k%div==0:
        iloc -= 1
    
    if iloc < 2:
        return one*iloc + five(n-1, k-(iloc*div))
    elif iloc == 2:
        return one*iloc
    else:
        return one*(iloc-1) + five(n-1, k-(iloc*div))
    
solution = lambda n, l, r:five(n, r)-five(n, l-1)