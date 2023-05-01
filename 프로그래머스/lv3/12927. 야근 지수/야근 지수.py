from collections import deque

def solution(n, works):
    work_hour, works = n, deque(sorted(works))

    def overtime_required():
        return True if sum([hour for hour in works]) > n else False
    
    if not overtime_required():
        return 0

    m_val, m_cnt = works.pop(), 1
    while works and work_hour > 0:
        new_value = works[-1]
        v_diff = m_val - new_value
        wh_need = v_diff * m_cnt
        if wh_need <= work_hour:
            work_hour -= wh_need
            m_val = works.pop()
            m_cnt += 1
        else:
            break

    m_val -= work_hour // m_cnt
    r_work_hour = work_hour % m_cnt
    answer = (m_val ** 2) * (m_cnt - r_work_hour) + ((m_val - 1) ** 2) * r_work_hour

    for w in works:
        answer += w ** 2

    return answer