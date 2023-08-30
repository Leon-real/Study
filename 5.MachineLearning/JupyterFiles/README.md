# ML 코딩

### 파일 목록
- 기초
    - [[기초] Linear Regression 선형회귀 - 회귀계수 확인하기](./Simple_Linear_Regression.ipynb)  
    - [[기초] KNN - K-최근접 이웃 - 스케일링](./Simple_KNN.ipynb)
- 간단한 예제
    - [Linear Regression 선형회귀 - 오존농도 예측](./LinearRegression_1(air_data).ipynb)  
    - [Linear Regression 선형회귀 - 보스턴 집값 예측](./LinearRegression_2(boston_data).ipynb)  
    - [Linear Regression 선형회귀 - 자동차 시트 판매량 예측](./LinearRegression_3(CarSeats).ipynb)  
    - [KNN k-최근접 이웃 알고리즘 - 대학 합격률 예측](./KNN_1(college_pass).ipynb)  
  
## Linear Regression 선형 회귀
- 평균으로 돌아가려는 경향이 있다는 가설을 바탕으로 분석하는 방법이다.  
- 최선의 회귀 모델은 전체 데이터의 **오차 합이 최소**가 되는 모델이다.
```python
# 단순 회귀의 회귀 계수
print(model.coef_) # 회귀계수(=가중치) 확인
print(model.intercept_) # 편향 수치 확인
```
```python
# 다중 회귀의 회귀 계수
print(list(x_train)) # 독립변수 이름 확인
print(model.coef_) # 회귀계수 확인
print(model.intercept_) # 편향 확인
```

## K-Nearest Neighbor K-최근접 이웃
- K개 값의 평균을 계산하여 값을 예측한다.(회귀)  
    - k값이 많아질수록 모델은 단순해진다.(왜냐하면 K값이 많아질수록 평균에 가까워지므로)  
- 가장 많이 포함된 유형으로 분류한다.(분류)  
- **적절한 K값**을 찾는 것이 중요하다.  
- 대표적인 스케일링 방법  
    - **주의 : 평가용 데이터도 학습용 데이터를 기준으로 스케일링을 수행한다.**  
    - 정규화 : 각 변수의 값이 0과 1 사이 값이 됌  
        $\large X_{norm}= \frac {x-x_{min}} {x_{max}-x_{min}}$  
    - 표준화 : 각 변수의 평균이 0, 표준편차가 1이 됌  
        $\large X_{z}= \frac {x-x_{mean}} {x_{std}}$  
## Decision Tree 결정 트리
- 의미 있는 질문을 먼저 하는 것이 중요하다.  
- 확률에 근거해 예측하는 것이다.  

## Logistic Regression
- (-∞, ∞)범위를 갖는 선형 판별식 결과로 (0,1) 범위의 확률 값을 얻게 된다.  
- 기본적으로 확률 값 0.5를 임계값으로 하여, 이보다 크면 1, 아니면 0으로 분류한다.  
