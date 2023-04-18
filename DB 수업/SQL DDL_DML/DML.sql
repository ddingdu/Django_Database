CREATE TABLE users (
  first_name TEXT NOT null,
  last_name TEXT NOT null,
  age INTEGER NOT null,
  country TEXT NOT null,
  phone TEXT NOT null,
  balance INTEGER NOT null
 );

-- user 테이블의 모든 컬럼 조회
SELECT * FROM users;

-- 이름과 나이 컬럼만 조회하기
SELECT first_name, age FROM users;

-- rowid와 이름 컬럼 조회하기
SELECT rowid, first_name FROM users;

-- 이름과 나이를 나이가 많은 순으로 정렬 (기본 값은 오름차순)
SELECT first_name, age FROM users ORDER BY age DESC;

-- 이름, 나이, 잔고를 나이가 적은 순, 잔고가 높은 순으로 정렬
SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;



-- 조회 결과 중복 제거하는 방법 : DISTINCT
SELECT DISTINCT country FROM users;

SELECT DISTINCT country FROM users ORDER BY country;

-- 조회 컬럼이 2개 이상인 경우
SELECT DISTINCT first_name, country FROM users;

SELECT DISTINCT first_name, country
FROM users
ORDER BY country;


-- 특정한 조건을 만족하는 결과 : WHERE 절 사용 (IF문)
SELECT first_name, age, balance
FROM users
WHERE age >= 30;

-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 
-- 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance
FROM users
WHERE age >= 30 AND balance > 500000;


-- : LIMIT
SELECT first_name, age, balance
FROM users
ORDER BY age
LIMIT 5 OFFSET 10;
-- LIMIT 20;














