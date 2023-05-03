def solution(lottos, win_nums):
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    low = rank[ len( set(lottos) & set(win_nums) ) ]
    high = rank[ len( set(lottos) & set(win_nums) ) + lottos.count(0) ]
    return [high, low]