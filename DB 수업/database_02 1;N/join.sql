-- SQLite
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    userid INTEGER,
    -- 외부 키 설정 / REFERENCES:외래 키가 누구를 참조하는지
    CONSTRAINT userid_fk FOREIGN KEY(userid) REFERENCES users(id)
);

CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roleid INTEGER NOT NULL
);

INSERT INTO users(name, roleid)
VALUES
('aiden', 1),
('ken', 3),
('lynda', 3),
('sophia', 2),
('beemo', 1),
('feel', 3),
('coco', 2);

-- DELETE FROM users
-- WHERE rowid > 7;

INSERT INTO articles(title, content, userid)
VALUES
('제목1', '내용1', 1),
('제목2', '내용2', 2),
('제목3', '내용3', 3),
('제목5', '내용5', 5),
('제목9', '내용9', 9),
('제목10', '내용10', 10);

-- DELETE FROM articles
-- WHERE rowid > 6;

-- FROM 절에 테이블 두개 넣어보기 (CROSS JOIN) 7*6=42
SELECT articles.* , users.*
FROM articles, users;

-- 두 테이블간에 공유하는 컬럼(외래 키) 사용하여 INNER JOIN
SELECT articles.* , users.*
FROM articles, users
WHERE articles.userid = users.id;

-- 두 테이블간에 조회를 하는데 왼쪽 테이블의 데이터는
-- 오른쪽과 매칭되는게 없어도 조회할 수 있도록 LEFT JOIN
SELECT articles.* , users.*
FROM articles LEFT JOIN users
ON articles.userid = users.id;

