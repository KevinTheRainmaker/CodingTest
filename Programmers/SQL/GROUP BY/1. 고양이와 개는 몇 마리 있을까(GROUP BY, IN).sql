-- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 
-- 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

-- 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS COUNT FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE
-- ANIMAL_TYPE에 CAT과 DOG만 있어서 정답인 것

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN('CAT','DOG')
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
-- WHERE절에서 매칭 확인은 ==이 아니라 = 사용
-- 또는 IN으로 튜플확인

-- COUNT([COLUMN NAME])의 경우 NULL을 무시하고 집계하므로 유의