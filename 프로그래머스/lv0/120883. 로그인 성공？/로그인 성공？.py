def solution(id_pw, db):
    db_dic = {data[0]:data[1] for data in db}
    ID, PW = id_pw[0], id_pw[1]

    if ID in db_dic:
        if db_dic[ID] == PW:
            answer = 'login' 
        else:
            answer = 'wrong pw'
    else:
        answer = 'fail'

    return answer