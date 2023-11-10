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
```sql
# name : collection 이름
db.createCollection(name, [option])
```
- option
    - capped : true로 설정하면 collection의 최대 용량을 설정
    - autoIndex : true로 설정하면 _id필드에 index가 자동으로 생성
    - size : 숫자 데이터를 사용하며 collection의 최대 사이즈를 byte단위로 지정
    - max : 숫자 데이터를 사용하여 최대 document갯수를 설정
```sql
# user 컬렉션을 생성
db.createCollection('user')
```
```sql
# autoIndex와 max옵션을 설정하여 info 컬렉션을 생성
db.createCollection("info1", {autoIndexId:true, capped:true, size:500, max:5})
```
#### 3-4 Make Document
```sql
db.<collection_name>.insert(<document>)
```
```sql
# 한번에 여러개의 document 추가
# max:5 옵션 제한에 걸려 5개의 데이터가 info1에 들어간다.
db.info1.insert( [
    { "subject":"python", "level":3 },
    { "subject":"web", "level":1 },
    { "subject":"sql", "level":2 },
    { "subject":"python", "level":3 },
    { "subject":"web", "level":1 },
    { "subject":"sql", "level":2 },
])
```
#### 3-5 Find
```sql
db.collection.find(query, projection)
```
- query : document 조회 조건을 설정. 모든 document를 조회 할때는 ({})를 사용
- projection : document를 조회할때 보여지는 필드(컬럼)를 정의

#### 3-6 query
- [참고 문서](https://www.mongodb.com/docs/v3.6/reference/operator/query/)  

#### 3-7 sort
- 'sort({key: value})' 와 같은 포멧으로 사용을 하며 key는 정렬할 필드명을 작성하고, value는 오름차순은 1, 내림차순을 -1을 넣어주면 된다..
```sql
# info 컬렉션의 document를 level 오름차순으로 정렬
db.info.find().sort({"level":1})
# info 컬렉션의 document를 level 내림차순으로 정렬
db.info.find().sort({"level":-1})
# level을 기준으로 내림차순으로 정렬한 후 subject를 기준으로 오름차순으로 정렬
db.info.find().sort({"level":-1, "subject":1})
```