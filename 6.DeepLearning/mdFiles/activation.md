# Activation 활성화 함수

활성화 함수에 회귀모델, 분류모델에 따라 함수(Softmax등..)를 넣으면,
회귀는 입력(결과값)을 그대로 전달  
분류는 입력(결과값)을 0~1(확률값)으로 바꿔서 전달  

- sigmoid 함수  
    - 0~1의 값  
- Leaky ReLU 함수  
    - max(0.1x, x)  
- tanh 함수  
    - tanh(x)  
- Maxout 함수  
    - max(w_1x+b1, x_2x+b2)  
- ReLU 함수  
    - max(0,x)  
- ELU 함수  
    - if x>=0이면 x,  
    - if x<0이면 α(e**x -1)  