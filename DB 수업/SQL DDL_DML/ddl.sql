-- 테이블 생성
CREATE TABLE contacts (
    name TEXT NOT NULL, 
    age INTEGER NOT NULL, 
    email TEXT NOT NULL UNIQUE
);

-- 테이블 구조 변경 : 테이블 이름 변경
ALTER TABLE contacts RENAME TO new_contacts;

-- 테이블 속성 이름 변경
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- 테이블 속성 추가, DEFAULT : 기존 값이 있을 경우, 기본 값을 무엇으로 할지 설정 
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';

-- 테이블 속성 삭제 (터미널에서 sqlite3 ddl.sqlite3 입력 후 복붙)
ALTER TABLE new_contacts DROP COLUMN address;

-- 테이블 삭제
DROP TABLE new_contacts;

