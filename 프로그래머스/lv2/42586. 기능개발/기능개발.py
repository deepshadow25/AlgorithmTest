from collections import deque
def solution(progresses, speeds):
    answer = []
    que = deque(progresses)
    while True:
        if not que:
            break
        for i in range(len(que)):
            que[i] += speeds[i]
        cnt = 0
        while True:
            if not que:
                answer.append(cnt)
                break
            if que[0] >= 100:
                que.popleft()
                del speeds[0]
                cnt += 1
            else:
                if cnt > 0:
                    answer.append(cnt)
                break
    return answer