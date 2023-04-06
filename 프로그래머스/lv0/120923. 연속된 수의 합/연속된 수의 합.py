def solution(num, total):
    if num%2 == 1:
        return [i for i in range((total//num)-int((num-1)/2), (total//num)+int((num-1)/2)+1)]
    else:
        return [i for i in range((total//num)-((num//2)-1), (total//num)+(num//2)+1)]