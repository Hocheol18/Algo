# 이름에 el이 들어가는 동물 찾기

- LIKE % 연산자 활용

        -- 'EL'이 들어가기만 하면 됨
        WHERE NAME LIKE '%EL%'
        결과: ANGEL, EL, ELLA, KELLY, SHELTER

        -- 'EL' 앞뒤로 반드시 한 글자 이상 있어야 함
        WHERE NAME LIKE '_%EL_%'
        결과: ANGEL, KELLY, SHELTER
        (EL, ELLA는 제외됨)

- 앞 뒤만 있는 연산자

        SELECT ANIMAL_ID, NAME
        FROM ANIMAL_INS
        WHERE NAME LIKE 'E%' OR NAME LIKE '%E'
        ORDER BY NAME;