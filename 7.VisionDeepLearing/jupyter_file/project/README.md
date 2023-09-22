
# 시각 지능 딥러닝 프로젝트  
'시각장애인' 및 '저시력자'등 시각의 보조가 필요한 사용자들에게  
스마트폰 카메라를 통해 화폐 정보를 알려주는 AI 모델 개발하기  
- [데이터 전처리](./DataProcessing.ipynb)  
- [YOLO이용 모델링](./modeling.ipynb)  
- [최종 테스트](./Test.ipynb)  
# 저시력자들을 위한 원화 화폐 분류  
- 데이터 출처 : [오픈데이터셋(selectstar)](https://open.selectstar.ai/ko/?page_id=5844)  
- 데이터 구분 : Image  
- 수행할 내용 : Object Detection  
- 사용 라이브리러 : ultralytics의 yolo

##### 주의할 점
실행파일과 폴더의 경로 및 이름 설정에 유의해주어야한다.  
특히 yaml파일의 경로 설정도 유의해야한다.  
```
폴더명(아무 폴더명이나 괜찮다.)  
ㄴimages : 이미지 파일들을 넣어높은 폴더(폴더명 똑같이 해주어야함)  
    ㄴtrain  
    ㄴval  
ㄴlabels : images안에 파일명과 매핑된, txt파일을 넣어놓은 폴더(폴더 명 똑같이해주어야함)  
    ㄴtrain   
    ㄴval  
```