# 워드 임베딩 Word Embedding

1. [워드 임베딩(Word Embedding)](#1-워드-임베딩word-embedding)
2. [워드 투 벡터(Word2Vec)](#2-워드-투-벡터word2vec)
3. [글로브(GloVe)](#3-글로브glove)
4. [패스트텍스트(FastText)](#4-패스트텍스트fasttext)
5. [엘모(ELMO)](#5-엘모elmo-embeddings-from-language-model)
6. [임베딩 벡터의 시각화(Embedding Visualization)](#6-임베딩-벡터의-시각화embedding-visualization)  
7. [영어/한국어 Word2Vec만들기](#7-영어한국어-word2vec만들기)  

## 1. 워드 임베딩(Word Embedding)
워드 임베딩(Word Embedding)은 단어를 벡터로 표현하는 방법으로,  
단어를 밀집 표현으로 변환한다.  

1. 희소 표현(Sparse Representation)  
    - 벡터 또는 행렬(matrix)의 값이 대부분이 0으로 표현되는 방법을 희소 표현(sparse representation)이라고 한다.  
    - 원-핫 벡터는 희소 벡터(sparse vector)  
    - 희소 벡터의 문제점 : 단어의 개수가 늘어나면 벡터의 차원이 한없이 커진다.
        - 이로 인해 벡터 표현은 공간적 낭비를 불러일으킨다.  
2. 밀집 표현(Dense Representation)  
    - 희소 표현과 반대되는 표현이다.  
3. 워드 임베딩(Word Embedding)  
    - 단어를 밀집 벡터(dense vector)의 형태로 표현하는 방법을 워드 임베딩(word embedding)이라고 한다. 그리고 이 밀집 벡터를 워드 임베딩 과정을 통해 나온 결과라고 하여 임베딩 벡터(embedding vector)라고도 한다.  
## 2. 워드 투 벡터(Word2Vec)
단어 벡터 간 유의미한 유사도를 반영할 수 있도록 단어의 의미를 수치화 할 수 있는 대표적인 방법이 워드투벡터(Word2Vec)이다.  
### 표현 방식
#### 분산 표현(Distributed Representation)
- 분산 표현(distributed representation) 방법은 기본적으로 분포 가설(distributional hypothesis)이라는 가정 하에 만들어진 표현 방법이다.  
- 이 가정은 '비슷한 문맥에서 등장하는 단어들은 비슷한 의미를 가진다' 라는 가정이다.  
-분산 표현은 분포 가설을 이용하여 텍스트를 학습하고, 단어의 의미를 벡터의 여러 차원에 분산하여 표현한다.  
- 단어의 의미를 여러 차원에다가 분산 하여 표현한다. 이런 표현 방법을 사용하면 단어 벡터 간 유의미한 유사도를 계산할 수 있다.

### 학습 방식
- 예문 : "The fat cat sat on the mat"

1. CBOW(Continuous Bag of Words)
- 주변에 있는 단어들을 입력으로 중간에 있는 단어들을 예측하는 방법이다.  
2. Skip-Gram
- 중간에 있는 단어들을 입력으로 주변 단어들을 예측하는 방법이다.  
## 3. 글로브(GloVe)
- 글로브(Global Vectors for Word Representation, GloVe)는 카운트 기반과 예측 기반을 모두 사용하는 방법론이다.
- 2014년에 미국 스탠포드대학에서 개발한 단어 임베딩 방법론
- 카운트 기반의 LSA, 예측 기반의 Word2Vec의 단점을 지적하고, 보완한다는 목적으로 나왔다.  
- 기존의 방법론
    - LSA
        - TF-IDF 행렬과 같이 각 문서에서의 **각 단어의 빈도수**를 카운트 한 행렬이라는 전체적인 통계 정보를 입력으로 받아 차원을 축소하여 잠재된 의미를 끌어내는 방법론이다.  
        - 전체적인 통계 정보를 고려한다.
        - 단어 의미의 유추 작업에는 성능이 떨어진다.
    - Word2Vec
        - **실제값과 예측값에 대한 오차를 손실 함수를 통해** 줄여나가며, 학습하는 예측 기반의 방법론
        - 단어 간 유추 작업에는 LSA보다 뛰어남
        - 임베딩 벡터가 윈도우 크기 내에서만 주변 단어를 고려하기 떄문에, 전체적인 통계 정보를 반영하지는 못한다.
- GloVe
    - 아이디어를 한 줄로 요약하면 '임베딩 된 중심 단어와 주변 단어 벡터의 내적이 전체 코퍼스에서의 동시 등장 확률이 되도록 만드는 것'이다.
    - 즉, 이를 만족하도록 임베딩 벡터를 만드는 것이 목표이다.
- GloVe 사용하기
    - GloVe 설치
        ```
        pip install glove_python_binary
        ```
    - 학습시키기
        ```python
        from glove import Corpus, Glove

        corpus = Corpus() 

        # 훈련 데이터로부터 GloVe에서 사용할 동시 등장 행렬 생성
        # 바로 아래 코드의 result는 토큰화된 결과물
        corpus.fit(result, window=5)
        glove = Glove(no_components=100, learning_rate=0.05)

        # 학습에 이용할 쓰레드의 개수는 4로 설정, 에포크는 20.
        glove.fit(corpus.matrix, epochs=20, no_threads=4, verbose=True)
        glove.add_dictionary(corpus.dictionary)
        ```
    - 유사한 단어들 리스트 리턴하기
        ```python
        print(glove.most_similar("man"))

        ```
## 4. 패스트텍스트(FastText)
- 페이스북에서 개발한, 단어를 벡터로 만드는 또 다른 방법이다.
- Word2Vec 이후에 나온 것이기 때문에, 메커니즘 자체는 Word2Vec의 확장이라고 볼 수 있다.
- Word2Vec의 가장 큰 차이
    - Word2Vec : 단어를 쪼개질 수 없는 단위로 생각한다.
    - FastText : 하나의 단어 안에도 여러 단어들이 존재하는 것으로 간주한다.
    - 내부 단어, 즉, 서브워드(Subword)를 고려하여 학습한다.  
    - 이로 인해 데이터 셋만 충분하다면, 내부 던어를 통해 모르는 단어에 대해서도 다른 단어와의 유사도를 계산할 수 있다는 장점이 있다.  
- FastText 사용하기
    - 라이브러리 불러오기
        ```python
        from gensim.models import FastText
        model = FastText(result, size=100, window=5, min_count=5, workers=4, sg=1)
        ```
    - 유사도 찾아보기
        ```python
        model.wv.most_similar("electrofishing")
        ```
## 5. 엘모(ELMO, Embeddings from Language Model)
- ELMo(Embeddings from Language Model)는 2018년에 제안된 새로운 워드 임베딩 방법론이다.
- 기존의 Word2Vec이나 GloVe의 경우 문맥에 따른 의미를 반영하지 못한다.
    - 예를 들어 Bank Account(은행 계좌)와 River Bank(강둑)에서 Bank는 전혀 다른 의미를 가진다.
- 따라서 문맥을 고려해서 임베딩을 하겠다는 아이디어가 문맥을 반영한 워드 임베딩이다.  
## 6. 임베딩 벡터의 시각화(Embedding Visualization)
- 구글은 임베딩 프로젝터(embedding projector)라는 데이터 시각화 도구를 지원한다.
- 워드 임베딩 모델로 부터 파일 생성하기
    ```python
    !python -m gensim.scripts.word2vec2tensor --input 모델이름 --output 모델이름
    ```
    - 위 코드 실행시, tsv파일이 만들어진다.
    - https://projector.tensorflow.org/ 사이트에서 좌측 상단에 Load 버튼을 클릭하여 2개의 tsv파일을 업로드 해준다.  
## 7. 영어/한국어 Word2Vec만들기 
- 사용되는 라이브러리
    ```python
    from gensim.models import Word2Vec
    from gensim.models import KeyedVectors
    ```
- Word2Vec 훈련시키기
    - vector_size = 워드 벡터의 특징 값. 즉, 임베딩 된 벡터의 차원.
    - window = 컨텍스트 윈도우 크기
    - min_count = 단어 최소 빈도 수 제한 (빈도가 적은 단어들은 학습하지 않는다.)
    - workers = 학습을 위한 프로세스 수
    - sg = 0은 CBOW, 1은 Skip-gram.
    ```python
    # result는 토큰화된 결과물
    model = Word2Vec(sentences=result, vector_size=100, window=5, min_count=5, workers=4, sg=0)
    ```
- Word2Vec 모델 저장하고 로드하기
    ```python
    model.wv.save_word2vec_format('eng_w2v') # 모델 저장
    loaded_model = KeyedVectors.load_word2vec_format("eng_w2v") # 모델 로드

    model_result = loaded_model.most_similar("man")
    print(model_result)
    ```
### 사전에 훈련된 Word2Vec 임베딩
- 라이브러리 및 모델 로드
    ```python
    import gensim
    import urllib.request

    # 구글의 사전 훈련된 Word2Vec 모델을 로드.
    urllib.request.urlretrieve("https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz", \
                            filename="GoogleNews-vectors-negative300.bin.gz")
    word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    ```
- 모델 크기 확인
    ```python
    print(word2vec_model.vectors.shape)
    ```
    ```python
    (3000000, 300)
    ```
    - 모델의 크기는 3,000,000 x 300이다. 즉, 3백만 개의 단어와 각 단어의 차원은 300입니다. 파일의 크기가 3기가가 넘는 이유를 계산해보면 아래와 같다.
    - 3 million words * 300 features * 4bytes/feature = ~3.35GB
    - 사전 훈련된 임베딩을 사용하여 두 단어의 유사도 계산해보기
        ```python
        print(word2vec_model.similarity('this', 'is'))
        print(word2vec_model.similarity('post', 'book'))
        ```
    - 단어 'book'의 벡터를 출력해보기
        ```python
        print(word2vec_model['book'])
        ```

## 임시