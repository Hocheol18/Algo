SELECT DISTINCT
   ID, EMAIL, FIRST_NAME, LAST_NAME 
FROM DEVELOPERS AS D
WHERE 
   D.SKILL_CODE & (SELECT SUM(CODE) 
                   FROM SKILLCODES 
                   WHERE CATEGORY = 'Front End') > 0
ORDER BY ID;