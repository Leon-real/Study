# softmax와 crossentropy  

## softmax 함수

입력 받은 값을 출력으로 0~1사이의 값으로 모두 정규화하여 출력 값들의 총합은 항상 1이 되는 특성을 가진 함수이다.    
소프트 맥스 결과값을 One Hot Encoder의 입력으로 입력하면 가장 큰 값만 True, 나머지는 False 값이 나오게 하여 이용 가능하다.  
  
- 출력은 0~1 사이의 실수이다.  
    - 출력을 '확률'로 해석할 수 있다.  
- 출력의 총합은 1이다.  
- 소프트맥스 활성화 함수를 적용해도 원소의 대소 관계는 변하지 않는다.  
    - 소프트맥스 활성화 함수에 사용되는 지수 함수가 단조 증가 함수이기 때문  
    - 즉, 출력층의 소프트맥스 활성화 함수는 생략해도 된다.  

## crossentropy

실제 분포 p에 대하여 알지 못하는 상태에서, 모델링을 통하여 구한 분포인 q를 통하여 p를 예측하는 것, q와 p가 모두 들어가서 크로스 엔트로피(cross-Entropy)라고 한다고 한다.   

머신러닝을 통한 예측 모형에서 훈련 데이터에서는 실제 분포인 p 를 알 수 있기 때문에 cross-entropy 를 계산할 수 있다. 즉, 훈련 데이터를 사용한 예측 모형에서 cross-entropy 는 실제 값과 예측값의 차이 (dissimilarity) 를 계산하는데 사용할 수 있다는 것이다.  

cross-entropy에서는 실제값과 예측값이 맞는 경우에는 0으로 수렴하고, 값이 틀릴경우에는 KL-Divergence만큼 값이 커지기 때문에, 실제 값과 예측 값의 차이를 줄이기 위해 사용한다. **cross-entropy의 값은 항상 entropy의 값보다 크다.**  