# AI Model Evaluation : AI 모델 평가와 해석

##### Jupyter Code Files : 코드 파일들
- [Review ML and DL : 머신러닝과 딥러닝 리마인드](./jupyterfiles/review_ML_DL.ipynb)  
- [Tree Model Feature importance : 트리 모델의 변수 중요도](./jupyterfiles/Tree_Model_feature_importance.ipynb)  
    - [Example : Attrition](./jupyterfiles/Feature_Importance_Example.ipynb)  

##### 모델 해석 방식 분류
![이미지](./images/Model_Evaluations.png)  

## PFI(Permutation Feature Importance) : 일반 모델의 변수 중요도
- 알고리즘과 상관 없이 변수 중요도를 파악할 수 있는 방법이다.
- Permutation(순열) : 순서가 부여된 임의의 집합을 다른 순서로 뒤섞는 연산
- Feature 하나의 데이터를 무작위로 섞을 때, model의 score가 얼마나 감소되는지로 계산한다.  

- Algorithm 구조
    - 특정 Feature j에 대해서, 여러번(K)시도(섞고, Score계산)해서 나온 Score의 평균 계산
    - $i_{j} = s - \frac{1}{K} \sum_{k=1}^{K} S_k,j$