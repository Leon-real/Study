# 웹 크롤링

- 웹 페이지에서 데이터를 수집하는 방법 
- 또한 이를 통하여, 데이터를 분석하고 레포팅하는 방법   

##### 예제 파일
[0. HTML 기초 및 Css Selector](./jupyterfile/0.Html_CssSelector_Basic.md)  
  ㄴ HTML 구성요소 및 구조와 Css Selector 기초 설명  
[1. 코스피, 코스닥, 환율 데이터 수집 및 분석](./jupyterfile/1.reuqests_and_analysis.ipynb)  
  ㄴ 코스피, 코스닥, 환율 데이터 수집 및 분석  
[2. response 에러 처리](./jupyterfile/2.response_error_handling.ipynb)  
  ㄴ requests를 하였을 때, response에 에러가 날 경우 처리  
[3. Using Api, api 사용법](./jupyterfile/3.UsingApi.ipynb)  
  ㄴ 네이버 파파고 api, 검색어 트렌드 api 활용하기  
[4. Final Pracice 최종 연습](./jupyterfile/4.Final_Crawling.ipynb)  
  ㄴ 직방 사이트의 부동산 매물 데이터 크롤링 및 모듈화하기  
[5. Module Test 모듈 테스트](./jupyterfile/5.module.ipynb)  
  ㄴ 4번에서 만든 모듈 사용해보기  
[6. 기타 여러 프로젝트](./jupyterfile/6.Several_Project.ipynb)  
  ㄴ 네이버 연관검색어 추출 및 저장하기  
  ㄴ Gmarket 베스트 상품 데이터 추출 및 저장하기  
### 웹페이지의 종류

- 정적인 페이지 : 웹 브라우저에 화면이 한번 뜨면 이벤트에 의한 화면의 변경이 없는 페이지  
- 동적인 페이지 : 웹 브라우저에 화면이 뜨고 이벤트가 발생하면 서버에서 데이터를 가져와 화면을 변경하는 페이지  

## 웹 크롤링 방법

1. requests 이용
    - **json 문자열**로 받아와서 파싱하는 방법 : 주로 **동적 페이지** 크롤링 할 때 사용  
    - **html 문자열**로 받아와서 파싱하는 방법 : 주로 **정적** **페이지** 크롤링 할 때 사용  
2. api 이용  
    - 각 사이트 내의 api 이용하여 데이터를 받는 방법(각 사이트별로 다르다.)  
3. selenium 이용
    - 브라우저를 직접 열어서 데이터를 받는 방법  

- 크롤링 방법에 따라 속도는  
requests json > requests html > selenium 순이다.(왼쪽일수록 빠른 속도)  
  
## 데이터 수집 절차

1. 웹 서비스 분석 : url
2. 서버에 데이터 요청 : request(url) > response : join(str)
3. 서버에서 받은 데이터 파싱(데이터 형태를 변경) : json(str) > list,dict > DataFrame
