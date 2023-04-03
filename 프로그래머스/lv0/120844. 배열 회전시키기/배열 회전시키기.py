def solution(numbers, direction):
    if direction == 'right':
        last = numbers.pop(len(numbers)-1)
        numbers.insert(0, last)
    if direction == 'left':
        first = numbers.pop(0)
        numbers.append(first)
    return numbers