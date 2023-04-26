-- 코드를 입력하세요 
SELECT member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d') as date_of_birth 
from member_profile
where month(date_of_birth) = 3 and TLNO is not null and gender = 'W'
order by member_id;
-- date_of_birth가 date type, format을 지정해 줘야 함. 그렇지 않으면 다르게 출력되는듯?
