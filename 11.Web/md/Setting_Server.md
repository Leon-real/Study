# Setting Server
##### 목차
- 기초
    - [Bash 기초 명렁어](#bash-기초-명렁어)
    - [Vim Editor](#vim-editor)
    - [TMUX(Terminal Multiplexer)](#tmuxterminal-multiplexer)
- 파일 설치 및(Python, jupyter, MongoDB, nginx) 서버 설정
    1. [서버접속](#서버접속)
    2. [환경설정 파일전송](#환경설정-파일전송)
    3. [파이썬 설치](#파이썬-설치)
    4. [주피터 노트북 설치 및 설정](#주피터-노트북-설치-및-설정)
    5. [주피터 노트북 서버에서 자바스크립트 커널 설정](#주피터-노트북-서버에서-자바스크립트-커널-설정)
    6. [MongoDB 설치](#mongodb-설치)
    7. [Nginx](#nginx)

## Bash 기초 명렁어
- `ls`
    - Description : 디렉토리의 파일리스트 출력
    - Example: ls -al
- `echo`
    - Description : 문자열 출력
    - Example : echo "hello world!"
- `touch`
    - Description : 파일 생성
    - Example : touch test.txt
- `mkdir`
    - Description : 디렉토리 생성
    - Example :
- `pwd`
    - Description : 현재 디렉토리 위치 출력
    - Example : pwd
- `cd`
    - Description : 디렉토리 이동
    - Example : cd ../test/notebooks
- `cat`
    - Description : 파일 안에 있는 텍스트 모두 출력
    - Example : cat test.txt
- `head`
    - Description : 파일 안에 있는 텍스트 상단 부터 출력
    - Example : head -n 10 test.txt
- `tail`
    - Description : 디렉토리 생성
    - Example : tail -n 10 test.txt
- `chmod`
    - Description : 파일 권한 수정
    - Example : chmod 400 test.txt
- `chown`
    - Description : 파일 소유자 수정
    - Example : chown -R ubuntu:ubuntu test.txt
- `History`
    - Description : 이전에 입력한 commands 히스토리 출력
    - Example : history
- `clear`
    - Description : 화면 초기화
    - Example : clear
- `cp`
    - Description : 파일 복사
    - Example : cp test.txt ../notebooks/
- `mv`
    - Description : 파일 이동, 파일 이름 바꾸기
    - Example : mv test.txt ../notebooks/test2.txt
- `ps`
    - Description : 프로세스 출력
    - Example : ps -e | grep note
- `kill`
    - Description : 프로세스 종료
    - Example : kill -9 1234
- `df`
    - Description : 하드 디스크의 남은 용량을 확인
    - Example : df -h
- `free`
    - Description : 현재 메모리 사용량 출려
    - Example : free -h
- `tree`
    - Description : 트리 형태로 디렉토리의 구조를 출력
    - Example : tree
- 특수 기호들
    - `|`
        - Description : 파이프라인 : 명령을 실행한 출력 결과에서 특정 조건으로 필터링하여 데이터를 출
        력
        - Example : history | grep ssh
    - `>`
        - Description : 출력 결과를 over write
        - Example : echo "hello world" > test.txt
    - `>>`
        - Description : 출력 결과를 append
        - Example : echo "hello world" >> test.txt
    - `&&`
        - Description : 연결해서 실행
        - Example : mkdir notebooks && cd notebooks
## Vim Editor
### Vim(vi improved) Editor
- 모든 Linux / Unix 시스템에서 사용할수 있는 문서 편집기
- 마우스 없이 키보드 입력으로 모든 기능사용 가능
- CLI(command line interface) 환경 또는 터미널 환경에서 사용
### Mode
- 일반모드
    - 문서의 특정 기능이나 위치로 이동할수 있는 모드
    - esc : 일반모드로 변경
    - w : forword : 단어 뒤로 이동
    - b : backword : 단어 앞으로 이동
    - ^ : 행의 가장 앞으로 이동
    - $ : 행의 가장 뒤로 이동
    - x : 현재 커서위치 문자 삭제
    - dw : 현재 커서 위치 단어 삭제
    - D : 현재위치에서 라인 끝까지 삭제
    - dd : 행삭제
    - gg : 문서 시작으로 이동
    - G : 문서의 끝으로 이동
    - 숫자 + G : 숫자 라인으로 이동
    - { : 이전 페이지로 이동
    - } : 다음 페이지로 이동
    - yw : 단어 복사
    - yy : 한줄 복사
    - p : 붙여넣기
    - u : 되돌리기
- 편집모드
    - 문서 내용을 편집할수 있는 모드
    - a : 커서 위치의 다음 칸부터 입력
    - i : 커서 위치 부터 입력
    - o : 커서 위치의 다음줄부터 입력
- 명령모드
    - 일반모드에서 : 입력하면 에디터 가장 마지막줄에 : 문자 뒤에 명령실행가능
    - / : 정방향 검색 , n : 다음 검색 단어로 이동
    - ? : 역방향 검색
    - w : write : 파일저장
    - q : quit : 나가기
    - ! : 강제실행
    - set number : 줄번호 표시
- 매크로
    - 매크로 작성 : q + 매크로이름(문자하나) + 매크로 키 입력 + q
    - 매크로 실행 : 매크로 실행횟수 + @ + 매크로이름
        - example) 행의 마지막에 , 붙이기
    - 매크로 작성 : q + a + $ + a + , + esc + (아래 화살표) + q
    - 매크로 실행 : 4 + @ + a
## TMUX(Terminal Multiplexer)
### Terminal Multiplexer
- Linux 접속 환경의 세션 관리
- 세션 : 접속정보를 저장하는 연결
- 윈도우 : 세션이 가지고 있는 여러개의 명령어 입력 환경
- 팬 : 윈도우가 가지고 있는 여러개의 분할된 화면
- 세션생성 : $ tmux new -s SamepleName(세션이름)
- 세션종료 : $ tmux kill-session -t SamepleName(세션이름)
- 세션 목록 보기 : $ tmux ls
- 세션접속 : $ tmux a -t SamepleName(세션이름)
- 윈도우생성 : $ ctrl + b, c
- 윈도우종료 : $ ctrl + b, &
- 윈도우이동 : $ ctrl + b, 0-9
- 팬생성(종분할) : ctrl + b, %
- 팬생성(횡분할) : ctrl + b, "
- 팬이동 : $ ctrl + b, 화살표 : $ ctrl + b, q (번호)
- 팬종료 : $ ctrl + b, x
## 서버접속
- ssh 명령을 이용하여 로컬 컴퓨터에서 서버 컴퓨터로 원격 접속
```bash
local $ ssh -i <pem file path> <user name>@<server public ip>

ex)
local $ ssh -i ~/.ssh/sample.pem ubuntu@54.180.1.46
```
## 환경설정 파일전송
- 구글 드라이브에서 env 디렉토리 다운로드 후 압축해제
```bash
local $ scp -ri <pem file path> <source file path> <user name>@<public ip>:<destination
file path>

ex)
local $ scp -ri ~/.ssh/sample.pem ~/Downloads/env ubuntu@54.180.1.46:~/
```
## 파이썬 설치
- 설정에서 선택하는 것이 나오면 모두 기본 값으로 설정 `<tap + enter>`
```bash
ubuntu $ source ~/env/pyenv.sh
```
- 파이썬 기본 버전을 3.8.5로 설정
```bash
ubuntu $ pyenv global 3.8.5
```
- requirments.txt에 정의된 파이썬 패키지 설치
```bash
ubuntu $ pip install -r ~/env/requirements.txt
```
## 주피터 노트북 설치 및 설정
- 주피터 노트북 설정 파일 생성
```bash
ubuntu $ jupyter notebook —generate-config
```
- 암호화된 패스워드 생성
```bash
ubuntu $ ipython
```
```python
In [1]: from jupyter_server.auth import passwd
In [2]: passwd()
Enter password: pw # 보안의 이유로 실제로 입력문자가 출력되지는 않음
Verify password: pw # 보안의 이유로 실제로 입력문자가 출력되지는 않음
Out[3]: 'sample_password'
In [4]: quit
```
- 주피터 노트북 서버 설정
```bash
ubuntu $ sudo vi /home/ubuntu/.jupyter/jupyter_notebook_config.py
```
```python
c.NotebookApp.ip = 'xxx.xx.x.xxx' # private ip address
c.NotebookApp.open_browser = False # 자동 브라우져 실행 설정
# 위에서 출력한 패스워드 설정
c.NotebookApp.password = 'sample_password'
——————————————————————————————————
```
## 주피터 노트북 서버에서 자바스크립트 커널 설정
- javascript 실행을 위한 패키지 설정
```bash
ubuntu $ sudo apt-get install nodejs npm jupyter
```
- ipython에서 실행 가능한 javascript를 npm으로 설치 및 설정
```bash
ubuntu $ sudo npm install -g --unsafe-perm ijavascript
ubuntu $ sudo ijsinstall --install=global
```
## MongoDB 설치
- 참고 자료 [링크](https://www.cherryservers.com/blog/install-mongodb-ubuntu-22-04)
- 설치 명령
```bash
ubuntu $ sudo apt install software-properties-common gnupg apt-transport-https cacertificates -y
ubuntu $ curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
ubuntu $ echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodbserver-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0
multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
ubuntu $ sudo apt update
ubuntu $ sudo apt install mongodb-org -y 
```
- MongoDB 서버 실행 및 실행확인
```bash
ubuntu $ sudo systemctl start mongod
ubuntu $ sudo systemctl status mongod
```
- Mongo shell 실행 및 관리자 계정 생성
```bash
ubuntu $ mongosh
```
```bash
test> use admin
switched to db admin
admin> db.createUser({ user: "SamepleName", pwd: "SamplePw", roles: [ "root" ] })
{ ok: 1 }
admin> quit
```
- 외부접속 허용 및 패스워드 사용설정
```bash
ubuntu $ sudo vi /etc/mongod.conf
```
```bash
# network interfaces
net:
    port: 27017
    bindIp: 0.0.0.0
# security:
security:
    authorization: enabled
```
- 설정 적용을 위한 MongoDB 서버 재시작
```bash
ubuntu $ sudo systemctl restart mongod
```
- 서버 접속 URI
```bash
URI : mongodb://<user>:<password>@<public ip>:<port>/?authSource=admin
URI : mongodb://SampleName:SamplePw@54.180.1.46:27017/?authSource=admin
```
## Nginx
- nginx 설치
```bash
ubuntu $ sudo apt-get install nginx
```
- nginx 실행 확인
```bash
ubuntu $ sudo systemctl status nginx
```
- nginx 설정
```bash
ubuntu $ sudo vi /etc/nginx/sites-available/default
```
- 정적 파일 설정
```bash
server {
    listen 8080;
    location / {
        root /home/ubuntu/html;
    }
}
```
- WAS 라우팅 설정
```bash
server{
    listen 8081;
    location / {
        proxy_pass http://localhost:5000;
    }
}
```
- 설정 적용을 위한 재시작
```bash
ubuntu $ sudo systemctl restart nginx
```