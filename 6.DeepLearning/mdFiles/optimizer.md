# Optimizer
- Gradient Descent (경사하강법) : 함수의 기울기(경사)를 구하여 함수의 극값에 이를 때까지 기울기가 낮은 쪽으로 반복하여 이동하는 방법.  
    ⇒ SGD (batch 학습)  
- Momentum (관성) : 이전에 이동했던 방향을 기억해서 다음 이동의 방향에 반영  
    ⇒ NAG  
- Adagrad (Adaptive Gradient) : 많이 이동한 변수(w)는 최적값에 근접했을 것이라는 가정하에 , 많이 이동한 변수(w)를 기억해서 다음 이동의 거리를 줄인다.  
    ⇒ RMSprop  
- Adam (RMSprop + Momentum)  