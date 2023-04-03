def solution(seoul):
    return [f'김서방은 {i}에 있다' for i in range(len(seoul)) if seoul[i] == "Kim"][0]