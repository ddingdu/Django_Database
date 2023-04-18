-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);


INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
    ('김', 30, '경기'),
    ('이', 31, '강원'),
    ('박', 26, '전라'),
    ('최', 12, '충청'),
    ('정', 28, '경상');

UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid=2;




SELECT COUNT(*) FROM users;

SELECT AVG(balance) FROM users;

SELECT * FROM users;

SELECT DISTINCT country FROM users;

SELECT country, avg(balance) FROM users
WHERE country = "전라북도";


SELECT country, avg(balance) FROM users
GROUP BY country ORDER BY avg(balance) DESC;

SELECT avg(age) FROM users
WHERE age >= 30;


SELECT country, COUNT(*) FROM users
GROUP BY country;

SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;

