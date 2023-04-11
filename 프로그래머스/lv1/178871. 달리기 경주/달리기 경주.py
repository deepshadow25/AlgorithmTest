def solution(players, callings):
    player = {play : idx+1 for idx, play in enumerate(players)}
    rank = {idx+1 : play for idx, play in enumerate(players)}
    
    for call in callings:
        current = player[call]
        previous = current - 1
        prev_player = rank[previous]
        
        rank[previous], rank[current] = rank[current], rank[previous]
        player[prev_player], player[call] = player[call], player[prev_player]
       
    return list(rank.values())
