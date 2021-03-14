-- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 
-- 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

-- 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 
-- 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.

SELECT animal_id, name, datetime from animal_ins order by name, datetime desc
-- name이 앞에 있으므로 먼저 정렬, 이후 name으로 정렬되지 않는 경우 뒤의 datetime으로 정렬됨

SELECT ANIMAL_ID, NAME, DATETIME from ANIMAL_INS ORDER BY 2, 3 DESC
-- 이처럼 인덱스(sql에선 파이썬 등의 프로그래밍 언어와 달리 인덱스가 1부터 시작)를 이용할 수도 있다