-- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 
-- 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

-- 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.

SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME
-- GROUP BY - HAVING 대신 WHRE을 사용할 경우 'Invalid use of group function'라는 에러가 발생한다.
-- 위 경우, 실행결과는 잘 나왔지만 사실상 부족한 부분이 있다.
-- NAME이 NULL인 것을 제외하지 않았다는 것이 문제점인데, 이 문제의 경우 2이상을 집계하는 것이라 보이지 않았던 것이다.

SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME
-- WHERE절로 NAME의 NULL 여부를 체크하는 구문 추가