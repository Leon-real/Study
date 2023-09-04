# Basic

### 기본 구조

0. 라이브러리 불러오기  
```python
import tensorflow as tf
```
1. 모델 구조 생성  
```python
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X,Y)
model.complie(loss='mse')
```
2. 모델 학습  
```python
model.fit(x_train, y_train, epochs=1000, verbos=0)
model.fit(x_train, y_train, epochs=10)
```

### 파일 목록  
- 기초
    - [레모네이드 판매 예측](./jupyter/basic/lemonade_sales_predict.ipynb)  
    - [아이리스 품종 예측](./jupyter/basic/iris_classification.ipynb)  
    - [보스톤 집 값 예측](./jupyter/basic//boston_house_price_predict.ipynb)  
    - [히든 레이어 활용 보스톤 집 값 예측](./jupyter/basic/hidden_layer.ipynb)  
