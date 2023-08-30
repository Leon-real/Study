# ML 코딩

### 파일 목록
- [Linear Regression 선형회귀 - 오존농도 예측](./LinearRegression_1(air_data).ipynb)  
- [Linear Regression 선형회귀 - 보스턴 집값 예측](./LinearRegression_2(boston_data).ipynb)  
- [KNN k-최근접 이웃 알고리즘 - 대학 합격률 예측](./KNN_1(college_pass).ipynb)  
  
## Linear Regression 선형 회귀
- 평균으로 돌아가려는 경향이 있다는 가설을 바탕으로 분석하는 방법이다.  
- 최선의 회귀 모델은 전체 데이터의 **오차 합이 최소**가 되는 모델이다.
```python
print(model.coef_) # 회귀계수(=가중치) 확인
print(model.intercept_) # 편향 수치 확인
```
```python
# 회귀계수 확인
print(list(x_train)) # 독립변수 이름 확인
print(model.coef_) # 회귀계수 확인
print(model.intercept_) # 편향 확인
```

## K-Nearest Neighbor K-최근접 이웃
- K개의 최근접 이웃의 값을 찾아 그 값들로 새로운 값을 예측하는 알고리즘
- 적절한 K값을 찾는 것이 중요하다.

## Decision Tree 결정 트리
- 의미 있는 질문을 먼저 하는 것이 중요하다.
- 확률에 근거해 예측하는 것이다.

## Logistic Regression
- (-∞, ∞)범위를 갖는 선형 판별식 결과로 (0,1) 범위의 확률 값을 얻게 된다.
- 기본적으로 확률 값 0.5를 임계값으로 하여, 이보다 크면 1, 아니면 0으로 분류한다.
