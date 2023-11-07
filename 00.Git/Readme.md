# Git
## 배운 내용
- 깃 사용법
- git graph 활용법(vscode 사용) ⇒ 브렌치 및 병합하기
- 브렌치 생성법, 병합, 충돌 처리 및 원격 저장 하는 법
  
  
---

## 1. Set Up

### git 명령어 형식

```bash
git [명령어] [옵션]
```

### 모든 config 설정 정보 보기

```bash
git config --list
global config 보기
git config --global --list
```

### 설정 정보 텍스트 에디터로 열기

```bash
git config -e
git config --global -e
```

### 사용자 설정

```bash
git config --global user.name 사용자이름
git config --global user.email 사용자이메일

등록 됬는지 확인
git config user.name
git config user.email

특정 프로젝트에서만 바꾸고 싶다면 해당 프로젝트로 이동해서 수정
git config user.name 사용자이름
git config user.email 이메일
```

## 2. Basic

### 깃 초기화

```bash
git init
```

git 폴더 안에 init을 했다면, `.git`이라는 숨겨진 폴더가 만들어지고 그 안에는 git 내부 구현 사항들이 저장되어 있다.

### 깃 폴더 열기와 삭제

```powershell
# 윈도우
start .git

# 맥
open .git

rm -rf .git
```

### 명령어의 옵션 확인하기

```bash
git 명령어 --h

// 얘시
git config --h
```

### 스테이징 하기

```bash
git add 파일
git add 파일 파일 파일 ...
git add *.txt  // txt 확장자 파일 모두 스테이징
git add * // 지워진 파일을 제외하고 나머지 모두 스테이징, 삭제된 파일이 있으면 삭제는 무시하고 나머지 스테이징
git add . // 모든 파일 스테이징, 삭제된 파일이 있다면 스테이징에도 삭제 처리
```

### 스테이징에서 working directory로 옮기기

```bash
git rm --cached 파일

// 예시
git rm --cached a.txt
git rm --cached *
```

### 특정 파일 무시하기

`.gitignore` 라는 파일 생성하고 그 파일 안에 무시할 파일명을 적어준다.  
git에서 더이상 추가, 추적하고 싶지 않는 파일들을 적어놓을 수 있다.  
  
- 만약 .gitignore에 추가해도 git에서 변화를 계속 감지할 경

```bash
git rm -r --cached .
git add .
git commit -m "Fix untracked files"
```

### 현재 상태 확인 status

```bash
git status  // 상세
git status -s // 간단하게
```

### 커밋하기

```bash
스테이징 상태에 있는 것 메시지와 함께 커밋하기
git commit -m "메시지"

추적중인 working directory와 스테이징에 있는 것 모두를 메시지와 함께 커밋하기
git commit -am "메시지"
```

### 현재 커밋의 변경 상태 확인하기

```bash
git commit -v
```

### log 활용법

```bash
git log
git log -p // 각 커밋마다의 변경사항 함께 보기
git log --oneline // 로그 한줄로 보기
git log --oneline --graph --all
git log -3 // 최근 커밋 3개만 보기
git log --oneline -3 // 원라인으로 최근 3개 커밋만 보기
git log --author="backtony" // 작성자가 backtony인것만 보기
git log --before="2020-09-08" // 날짜 이전의 커밋로그 보기
git log --grep="project" // 커밋메시지 중 project가 포함된 커밋만 보기
git log -S "about" // 커밋중 소스코드 컨텐츠 안에서 about이라는 코드가 변경사항에 있는 커밋 찾기
git log -S "about" -p // 커밋중 소스코드 컨텐츠 안에서 about이라는 코드가 변경사항에 있는 커밋 자세히 보기
git log about.txt // about.txt 파일에 대한 커밋 로그 보기
git log -p about.txt // about 파일에 대한 커밋 로그 자세히 보기
git log HEAD~1 // HEAD의 이전 커밋부터 로그 보기
git log HEAD~2 // HEAD의 2번째 전 커밋부터 로그 보기
git show 해시코드 // 커밋에 해당하는 정확한 내용 확인, 해시코드 적당히 붙여넣으면 된다. 전부를 복붙하지 않아도됨
git show 해시코드:파일명 // 커밋에 여러 내용이 있을 때 특정 파일에 대한 정보만 확인
git diff 해시코드 해시코드  // 두가지 커밋에 대한 비교
git diff 해시코드 해시코드 파일 // 두가지 커밋에서 해당 파일에 대한 비교
```

## 3. 깃허브

### 깃허브 프로젝트 내 pc에 가져오기

```bash
git clone 복사한주소 // 리포지토리 원격에서 받아오기
git remote // 원격서버에 관련된 정보, 기본적 서버 이름은 origin
git remote -v // origin이 정확히 어떤것을 가리키는지 확인
git remote add 만들서버이름 주소 // origin 말고 다른 원격 서버원격 저장소 설정
git remote show // 원격저장소 정보
git remote show 서버이름 // 서버의 자세한 정보
git remote rm 원격저장소명(예를들면 origin) // 연결된 원격 제거
```

### 내 커밋 서버에 저장하기

```bash
git push
git push -f // 충돌이 났을때 서버 작업을 무시하고 local것으로 대체
```

### 이미 만들어진 프로젝트 깃허브에 업로드하기

```bash
git remote add origin 리포지토리주소
git push // main에 푸시
```

### fetch와 pull

git에서 local과 github와 함께 연동해서 작업하는 경우 나의 local에서는 github에 있는 branch를 origin이라고 표기한다. origin/master와 master이 현재 b를 가리키고 있는 상황에서 github에서 새로운 commit이 발생하여 서버의 origin/master은 c를 가리키고 있다고 해보자.

이때 fetch를 사용하면 서버에 있는 git history를 받아와서 나의 local git history를 업데이트 하게 된다. 그럼 local에서 b를 가리키고 있던 origin/master은 c를 가리키게 되지만 local에서 내가 현재 바라보고 있는 작업 환경 HEAD는 그대로 유지된다. 즉, github에 업데이트된 내용을 로컬에 내려받는 것은 아니고 어디까지 업데이트 됬는지 확인만 하도록 하는 것이다.

반면에 pull의 경우 fetch + merge(옵션에 따라 rebase) 작업을 한번에 하는 것이다. github의 history를 가지고 와서 나의 local에 있는 내용을 함께 merge를 하게 된다. 따라서 origin master와 나의 master이 모두 c를 가리키게 된다.

fetch의 경우에는 서버의 history를 업데이트해서 어떤 작업이 일어나고 있는지 확인하고 싶을 때 사용되고, 서버에 있는 내용을 받아와서 나의 local 버전도 서버와 동일하게 만들고 싶을 때 pull을 사용한다.

fetch를 하면 아직 로컬에 받아온 것은 아니지만, git checkout origin/master 을 이용해서 해당 코드 내역을 확인할 수 있다.