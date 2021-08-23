SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%EL%'
ORDER BY NAME ASC;

-- Like, %, - 사용하여 해결
-- % = 여러개의 문자 매칭
-- - = 한개의 문자 매칭
-- https://programmers.co.kr/learn/courses/30/lessons/59047