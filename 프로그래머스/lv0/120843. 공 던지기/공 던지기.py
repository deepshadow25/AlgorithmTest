def solution(numbers, k):
    if len(numbers) % 2 == 0:
        players = numbers[0::2]
    else:
        players = numbers[0::2] + numbers[1::2]
    return players[(k%len(players))-1]