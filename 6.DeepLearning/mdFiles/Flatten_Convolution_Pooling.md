## Flatten  
- 입력 데이터를 1차원으로 평탄화(faltten)하는 것이다.  
- 2D 혹은 3D의 특징 맵(feature map)을 1D 벡터로 변환하여, 이후의 레이어에서 처리하기 쉽게 만들어주는 역할을 한다.  
```python
# 모델 생성
X = tf.keras.Input(shape=[28 * 28])
H = tf.keras.layers.Flatten()(X)
H = tf.keras.layers.Dense(84, activation="swish")(H)
Y = tf.keras.layers.Dense(10, activation="softmax")(H)

model = tf.keras.Model(X, Y)
model.compile(loss="categorical_crossentropy", metrics="accuracy")
model.summary()
```
## Convolution(합성곱)  
- 커널(kernel)또는 필터(filter)라는 $n * m$크기의 행렬로 $높이(height) * 너비(width)$ 크기의 이미지를 처음부터 끝까지 겹치며 훑으면서 $n * m$크기의 겹쳐지는 부분의 각 이미지와 커널의 원소의 값을 곱해서 모두 더한 값을 출력하는 것을 말한다.(이때 이미지의 가장 왼쪽 위부터 가장 오른쪽 아래까지 순차적으로 훑는다.)  
```python
# 모델 생성

X = tf.keras.Input(shape=[28,28,1])
H = tf.keras.layers.Conv2D(3, kernel_size=5, activation='swish')(X)
H = tf.keras.layers.Conv2D(6, kernel_size=5, activation='swish')(H)
H = tf.keras.layers.Flatten()(H)
H = tf.keras.layers.Dense(84, activation='swish')(H)
Y = tf.keras.layers.Dense(10, activation='softmax')(H)

model = tf.keras.Model(X,Y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')
model.summary()
```
## Pooling  
풀링 층에서는 특성 맵을 다운샘플링하여 특성 맵의 크기를 줄이는 풀링 연산이 이루어진다.  
풀링 연산에는 일반적으로 최대 풀링(max pooling)과 평균 풀링(average pooling)이 사용된다.  
- Max pooling  
    - 특징맵을 다운 샘플링하여 특징 맵의 크기를 줄이는 풀링연산을 말한다. 이때, 커널과 겹치는 영역 안에서 최대값을 추출하는 방식으로 다운 샘플링을 한다.  
- Average pooling  
    - 특징맵을 다운 샘플링하여 특징 맵의 크기를 줄이는 풀링연산을 말한다. 이때, 커널과 겹치는 영역 안에서 평균값을 추출하는 방식으로 다운 샘플링을 한다.  
```python
# 모델 생성
X = tf.keras.Input(shape=[28, 28, 1])
H = tf.keras.layers.Conv2D(3, 5, activation='swish')(X)
H = tf.keras.layers.MaxPool2D()(H)
H = tf.keras.layers.Conv2D(6, 5, activation='swish')(H)
H = tf.keras.layers.MaxPool2D()(H)
H = tf.keras.layers.Flatten()(H)
H = tf.keras.layers.Dense(84, activation='swish')(H)
Y = tf.keras.layers.Dense(10, activation='softmax')(H)

model = tf.keras.Model(X, Y)
model.compile(loss="categorical_crossentropy", metrics="accuracy")
model.summary()
```
### 파일 목록
- [Flatten](../jupyter/flatten_convolution_pooling/MNIST_Flatten.ipynb)  
- [Convolution](../jupyter/flatten_convolution_pooling/MNIST_Convolution.ipynb)  
- [Pooling](../jupyter/flatten_convolution_pooling/MNIST_MaxPool.ipynb)  