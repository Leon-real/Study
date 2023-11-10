# DataBase 데이터베이스 기초
##### 목차
1. [데이터베이스 기초 설명](#데이터베이스-기초-설명)  
2. [MongoDB 기초](#mongodb)  

## 데이터베이스 기초 설명
- DataBase (DB)  
    - 데이터를 통합하여 관리하는 데이터의 집합  
- DataBase Manage System (DBMS)  
    - 데이터베이스를 관리하는 미들웨어 시스템을 데이터베이스 관리시스템  
- Relational Database Management System (RDBMS)  
    - 데이터 테이블 사이에 키값으로 관계를 가지고 있는 데이터베이스  
    - Oracle, Mysql, Postgresql, Sqlite 등  
    - 데이터 사이의 관계 설정으로 최적화 된 스키마를 설계 가능  
    - `데이터 분류, 정렬, 탐색속도가 빠름`  
    - `오래 사옹된 만큼 신뢰성이 높음`  
    - `스키마수정이 어려움`  
- NoSQL  
    - 데이터 테이블 사이에 관계가 없이 저장하는 데이터베이스    
    - 데이터 사이의 관계가 없으므로 복잡성이 줄고 많은 데이터의 저장 가능    
    - `RDBMS의 한계를 극복하기 위해 만들어진 데이터 베이스`  
    - `확정성이 좋음 - 데이터의 분산처리 용이`  
    - `데이터 저장이 유연함 - RDBMS와 다르게 구조의 변경이 불필요`  
    - `스키마 및 Join이 없음`  
    - `Key-Value 형태의 JSON 포멧`  
    - `Select는 RDBMS보다 느리지만 Insert가 빨라 대용량 데이터 베이스에 많이 사용된다.`  
## MongoDB

### 1. MongoDB 설치
- [설치경로](https://studio3t.com/download-studio3t-free/)를 통해 Studio 3T 다운로드후 설치한다.

### 2. Connection 연결하기
1. 설치된 파일을 실행시킨다.
2. 좌측 상단의 `connect`클릭
3. `New Connection` 클릭
4. 접속정보 입력 후 Next 클릭
```bash
mongodb://<USERNAME>:<PASSWORD>@<HOST>:27017/?authSource=admin

# ex)
mongodb://samplename:samplepassword@xx.xxx.x.xxx:27017/?authSource=admin
```
### 3. Basic Syntax 기본 문법
- [MongoDB 참고 문서](https://www.mongodb.com/docs/v3.6/reference/)
#### 3-1 Create Database
```sql
# mongo 라는 이름의 데이터 베이스 생성
use mongo
```
```sql
# 현재 사용중인 데이터 베이스 확인
db
```
```sql
# database list 확인
show dbs
```
```sql
# document 생성
use mongo
db.user.insert({"name":"alice", "age":"90", "email":"test@sample.com"})
```
#### 3-2 Delete Database
```sql
# 현재 사용중인 데이터 베이스 삭제
db.dropDatabase()
```
#### 3-3 Create Collection
