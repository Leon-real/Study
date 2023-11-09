# Setting Server
##### 목차
1. [서버접속](#서버접속)
2. [환경설정 파일전송](#환경설정-파일전송)
3. [파이썬 설치](#파이썬-설치)
4. [주피터 노트북 설치 및 설정](#주피터-노트북-설치-및-설정)
5. [주피터 노트북 서버에서 자바스크립트 커널 설정](#주피터-노트북-서버에서-자바스크립트-커널-설정)
6. [MongoDB 설치](#mongodb-설치)
7. [Nginx](#nginx)

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
In [3]: quit
```
- 주피터 노트북 서버 설정
```bash
ubuntu $ sudo vi /home/ubuntu/.jupyter/jupyter_notebook_config.py
```
## 주피터 노트북 서버에서 자바스크립트 커널 설정
## MongoDB 설치
## Nginx