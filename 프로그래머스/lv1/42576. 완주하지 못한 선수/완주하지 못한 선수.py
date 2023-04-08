def solution(participant, completion):
    participant.sort()
    completion.sort()
    for idx, play in enumerate(completion):
        if play != participant[idx]:
            return participant[idx]
    return participant[-1]