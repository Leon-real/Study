# Css
##### 목차
- [Css Selector](#css-selector)  
- [Text Style](#text-style)  
- [Layout Style](#layout-style)  
## Css Selector
- 엘리먼트를 선택하는 방법
    - Tag 이름으로 선택 : tag 이름 앞에 아무 문자 없이 태그 이름으로 선택
    - ID 이름으로 선택 : ID 이름 앞에 # 을 사용하여 ID 이름으로 선택
    - Class 이름으로 선택 : Class 이름 앞에 . 을 사용하여 Class 이름으로 선택
    - Attribute 이름으로 선택 : Attribute 데이터를 [ ]로 감싸서 선택
- 계층적으로 엘리먼트를 선택하는 방법
    - 한단계 하위 엘리먼트에서 선택 : Selector 사이에 > 를 사용하여 엘리먼트 선택
    - 모든 하위 엘리먼트에서 선택 : Selector 사이에 공백문자를 사용하여 엘리먼트 선택
- 특별하게 엘리먼트를 선택하는 방법
    - not selector : 특정 엘리먼트만 제외하여 엘리먼트 선택
    - first-child selector : 여러개의 엘리먼트에서 첫번째 엘리먼트 선택
    - last-child selector : 여러개의 엘리먼트에서 마지막 엘리먼트 선택
    - nth-child selector : 여러개의 엘리먼트에서 n번째 엘리먼트 선택
    - before : 선택한 엘리먼트 앞에 있는 엘리먼트 선택
    - After : 선택한 엘리먼트 뒤에 있는 엘리먼트 선택
- 여러개의 Selector를 사용하여 선택하는 방법
    - , 를 사용하여 여러개의 엘리먼트 선택
    - Selector를 붙여쓰면 and의 의미를 가짐
## Text Style
- 웹폰트 사용
    - Reference : https://fonts.google.com/
- 다운로드 폰트 사용
    - Reference : https://github.com/naver/d2codingfont
        ```css
        @font-face {
        font-family: 'font-name';
        src: url('link');
        }```
- 글꼴 설정
    - font-family : 글꼴 설정
    - color : 글자 색상 설정 : rgb, rgba 설정 가능
    - font-size : 글자 크기 설정 : 주로 px 사용
    - font-style : 글자 스타일 설정 : normal, italic
    - font-weight : 글자 굵기 설정 : normal, bold, lighter, 100 ~ 900
    - line-height : 글자 세로 간격 설정
    - letter-pacing : 글자 가로 간격 설정
    - text-align : 글자 정렬 : left, right, center ...
    - text-decoration : 텍스트의 밑줄이나 취조선 설정
## Layout Style
- 레이아웃 영역설정
    - margin : border 바깥 영역의 여백 설정
        - 여백 설정 예시
        - 5px : 모든 margin 5px
        - 5px 10px : 위아래 5px, 좌우 10px
        - 5px 10px 15px 20px : top에서 시계방향으로 5px 10px 15px 20px
    - border : 영역의 테두리 설정
        - border style : solid, dotted, dashed ...
    - border-radius : 둥근 모서리 설정
    - padding : border 안쪽 영역의 여백 설정
    - width : 컨텐츠의 가로길이 설정 : px, %, auto
    - height : 컨텐츠의 세로길이 설정
- 레이아웃 정렬
- float : 레이아웃 정렬 설정 : left, right
    - float 은 레이아웃의 높이값이 0으로 설정됨
- display : 레이아웃 출력 속성 설정 : block, inline-block
    - inline-block 은 block 설정된 상위 엘리먼트를 기준으로 정렬
- position : 레이아웃 위치 설정
    - relative : 문서 흐름(바로 이전 레이아웃)에 맞춰서 레이아웃 위치 지정
    - absolute : relative로 설정된 상위 레이아웃 기준으로 위치 지정
    - fixed : 브라우져 document를 기준으로 위치 지정
- 배경 설정
    - background-color : 배경색 설정
    - background-image : 이미지 파일을 배경으로 설정
    - background-position : 이미지 파일의 배경 위치 설정 : left right center top botton