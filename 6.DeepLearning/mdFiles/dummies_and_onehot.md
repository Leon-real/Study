# 가변수화와 one-hot인코딩의 차이

get_dummies를 통한 가변수화의 경우, 변수의 개수가 4개일 때, 가변수화를 수행하면 변수가 3개가 된다.  

one-hot 인코딩의 경우 변수의 개수가 4개일 때, 원핫인코딩을 수행하면 변수가 4개가 된다.  

**가변수화를 하는 이유는 분석에 이용하기 위하여 하기 때문**이다.  

즉, 간단하게 이해하자면,  
**독립 변수는 dummy,  
종속 변수는 one-hot**  

### 가변수화 사용법
```python
import pandas as pd
df = pd.DataFrame({"test":["a","b","c"]})
pd.get_dummies(df['test'],drop_first=True)

```
### 원핫 인코딩 사용법
```python
import pandas as pd
df = pd.DataFrame({"test":["a","b","c"]})
pd.get_dummies(df['test'])
```