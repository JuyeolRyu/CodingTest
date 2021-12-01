SELECT NAME,DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (
    SELECT ANIMAL_ID
    FROM ANIMAL_OUTS
)
ORDER BY DATETIME
LIMIT 3

--oracle
SELECT name,datetime
from animal_ins
where animal_id not in (select animal_id from animal_outs)
order by datetime
FETCH NEXT 3 ROWS ONLY;
