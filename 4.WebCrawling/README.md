# 웹 크롤링

- 웹 페이지에서 데이터를 수집하는 방법 
- 또한 이를 통하여, 데이터를 분석하고 레포팅하는 방법   

##### 예제 파일
[1. 코스피, 코스닥, 환율 데이터 수집 및 분석](./1.reuqests_and_analysis.ipynb)  
  ㄴ 코스피, 코스닥, 환율 데이터 수집 및 분석  
[2. response 에러 처리](./2.response_error_handling.ipynb)  
  ㄴ requests를 하였을 때, response에 에러가 날 경우 처리  
[3. Using Api, api 사용법](./3.UsingApi.ipynb)  
  ㄴ 네이버 파파고 api, 검색어 트렌드 api 활용하기

### 웹페이지의 종류

- 정적인 페이지 : 웹 브라우저에 화면이 한번 뜨면 이벤트에 의한 화면의 변경이 없는 페이지  
- 동적인 페이지 : 웹 브라우저에 화면이 뜨고 이벤트가 발생하면 서버에서 데이터를 가져와 화면을 변경하는 페이지  

## 웹 크롤링 방법

1. requests 이용
    - **json 문자열**로 받아와서 파싱하는 방법 : 주로 **동적 페이지** 크롤링 할 때 사용  
    - **html 문자열**로 받아와서 파싱하는 방법 : 주로 **정적** **페이지** 크롤링 할 때 사용  
2. selenium 이용
    - 브라우저를 직접 열어서 데이터를 받는 방법  

- 크롤링 방법에 따라 속도는  
requests json > requests html > selenium 순이다.(왼쪽일수록 빠른 속도)  
  
## 데이터 수집 절차

1. 웹 서비스 분석 : url
2. 서버에 데이터 요청 : request(url) > response : join(str)
3. 서버에서 받은 데이터 파싱(데이터 형태를 변경) : json(str) > list,dict > DataFrame
  
## Response Error 처리하기
1. user-agent 수정하기  
2. referer 수정하기  