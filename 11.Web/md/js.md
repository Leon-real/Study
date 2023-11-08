# JavaScript 자바스크립트
- 웹브라우져에서 동작되는 동적으로 웹페이지를 바꾸고 이벤트를 처리하는 언어
- 인터프리터, 동적타이핑, 객체지향
##### 목차
1. [변수선언](#변수선언)
2. [데이터타입](#데이터타입)
3. [연산자](#연산자)
4. [조건문](#조건문)
5. [반복문](#반복문)
6. [함수](#함수)
7. [객체](#객체)

## 변수선언
- 식별자 : 저장공간을 구분하는 문자열
- 식별자 규칙
    대소문자, 숫자, _ , $ 사용가능  
    숫자 가장 앞에 사용 X  
    예약어 사용 X  
- 식별자 컨벤션  
    상수 : UPPER_SNAKE_CASE  
    변수 : camelCase  
    함수 : camelCase  
    모듈 : PascalCase  
```javascript
// 식별자 1개, 데이터 1개
var data1 = 10;
var data2 = 'js';
// 식별자 n개, 데이터 n개
var data3 = 20, data4 = 'node';
var data3 = 20,
 data4 = 'node';
// 식별자 n개, 데이터 1개
var data5 = data6 = 'web';

// console.log() : 식별자 데이터 출력
console.log(data1, data2, data3, data4, data5, data6);
// 10 'js' 20 'node' 'web' 'web'
``` 
## 데이터타입
- number : 숫자 데이터 타입(정수, 실수)
- string : 문자열 데이터 타입
- boolean : 논리값 데이터 타입
- function : 코드 저장하는 함수 데이터 타입
- object : 객체를 저장하는 데이터 타입
```javascript
var data1 = 1;
var data2 = 'javascript';
var data3 = true;
var data4 = function(){ console.log('function'); };
var data5 = {key: 'value'};

// typeof : 함수가 아닌 명령어
// 동적타이핑 : 데이터에 따라서 자동으로 데이터 타입 설정
console.log(typeof data1, typeof data2, typeof data3)
console.log(typeof data4, typeof data5)

// number string boolean
// function object
```
- 없는 데이터의 표현
    - undefined : 선언은 되었으나 값이 할당되지 않음
    - null : 선언이 되어 값이 없음이 할당됨
    - NaN : Number 데이터 타입에서의 undefined, 0/0
```javascript
var data = undefined;
console.log(typeof data, data);
// undefined undefined

var data = null;
console.log(typeof data, data);
// object null

var data = NaN;
console.log(typeof data, data);
// number NaN

// NaN 데이터 타입은 비교연산하면 항상 NaN 출력
console.log(NaN == NaN, NaN > NaN);
// false false
```
- 데이터 타입의 형변환
    - Number() : 숫자 데이터 타입으로 변환
    - String() : 문자열 데이터 타입으로 변환
    - Boolean() : 논리값 데이터 타입으로 변환
```javascript
var data1 = '1';
var data2 = 2;
console.log(typeof data1, data1);
console.log(typeof Number(data1), typeof Boolean(data1));
// string 1
// number boolean

console.log(data1 + data2, Number(data1) + data2, data1 + String(data2));
// 12 3 12
```
- 묵시적 형변환
    - 여러 데이터 타입을 혼합해서 연산하면 묵시적 형변환이 발생함(파이썬은 에러발생)
```javascript
onsole.log(typeof data1, typeof data2);
console.log(typeof (data1 + data2));
// string number
// string

// 문자 > 숫자
console.log(typeof data1, typeof (data1 - 0));
// string number

// 숫자 > 문자
console.log(typeof data2, typeof ('' + data2));
// number string
```
## 연산자
- 산술 : 데이터 + 데이터 = 데이터 : +, -, *, /, %, **, ++, --
- 비교 : 데이터 + 데이터 = 논리값 : ==, ===, !=, !==, <, >, <=, >= : 조건 1개
- 논리 : 논리값 + 논리값 = 논리값 : !, &&, || : 조건 2개 이상
- 할당 : 변수 산술= 데이터 : 변수에 누적해서 연산
- 삼항 : (조건) ? (참) : (거짓) : 간단한 조건문 구현
```javascript
// 산술연산자
var data1 = 11, data2 = 4;
console.log(data1 / data2, data1 % data2, data2 ** 3);

// 2.75 3 64
```
```javascript
// ++data : +1하고 대입
data1 = ++data2;
console.log(data1, data2);
// data++ : 대입하고 +1
data1 = data2++;
console.log(data1, data2)

// 5 5
// 5 6
```
```javascript
// 비교연산자
// ===, !==: 데이터 타입까지 비교
// ==, != : 데이터만 비교
var data1 = 1, data2 = '1';
console.log(data1, data2)
console.log(data1 === data2, data1 == data2, data1 != data2, data1 !== data2)

// 1 '1'
// false true false true
```
```javascript
// 논리연산자
console.log(true && false, true || false)

// false true
```
```javascript
// 할당연산자
var data1 = 10;
// data1 = data1 + 5;
data1 += + 5;
console.log(data1);

// 15
```
```javascript
// 삼항연산자 : (조건)?(참):(거짓)
var balance = 10000, withdraw = 6000;
var msg = balance >= withdraw ? '인출가능' : '인출불가';
console.log(msg)

// 인출가능
```
## 조건문
- if, else if, else
- switch, case, default
```javascript
// 학점출력 : if, else if, else
var point = 87;
if(point >= 90){
 console.log('A');
} else if(point >= 80){
 console.log('B');
} else if(point >= 70){
 console.log('C');
} else if(point >= 60){
 console.log('D');
} else{
 console.log('F');
}

// B
```
```javascript
// 승점출력 : switch, case, default
var point = '승';
switch(point){
 case '승':
 console.log('승점', 3);
 break;
 case '무':
 console.log('승점', 1);
 break;
 default:
 console.log('승점', 0);
}

// 승점 3
```
## 반복문
- while, for, break, continue
```javascript
var count = 3;
while (count > 0){
 count -= 1;
 console.log('js');
}

// js
// js
// js
```
```javascript
for(var i = 0; i < 3; i++){
 console.log('js');
}

// js
// js
// js
```
```javascript
// break, continue
for(var i = 0; i < 5; i++){
 if(i === 2){
 continue;
 }
 console.log(i, 'js');
 if(i >= 3){
 break;
 }
}

// 0 'js'
// 1 'js'
// 3 'js'
```
## 함수
- 중복코드를 묶어서 코드 작성 및 실행 : 코드 유지보수 증대
- 사용법 : 함수선언(코드작성) > 함수호출(코드실행)
- function, argument, parameter, 표현식, 선언식, hoisting, scope, 익명함수, return
```javascript
// 함수선언 : 코드작성
function showLotto(){
 var count = 6, lotto = '';
 for(var i = 0; i < count; i++){
 var randomNumber = Math.ceil(Math.random() * 44) + 1;
 lotto = lotto + randomNumber;
 if(i !== count - 1) lotto += ' ';
 };
 console.log(lotto);
};

// 함수호출 : 코드실행
showLotto();
```

```javascript
// argument, parameter : 함수 호출시 함수 선언하는 코드로 데이터 전달
function showLotto(count){
 var lotto = '';
 for(var i = 0; i < count; i++){
 var randomNumber = Math.ceil(Math.random() * 44) + 1;
 lotto = lotto + randomNumber;
 if(i !== count - 1) lotto += ' ';
 }
 console.log(lotto);
};
// 로또번호 출력 : 6개
showLotto(6);
```
- hoisting : 호이스팅
    - 선언식으로 변수(함수)가 선언되면 코드의 최상단으로 올라가서 선언됨
    ```javascript
        // 선언식은 함수 호출 후에 함수가 선언되어도 함수 호출 가능
    plus4(1, 2);
    function plus4(n1, n2){
    console.log(n1 + n2)
    };

    // 3
    ```
- scope : 스코프
    - 함수밖 : 전역변수 : global
    - 함수안 : 지역변수 : local
    ```javascript
    var data = 10;
    function change(){
    data = 20; // var 사용하지 않으면 전역변수로 사용
    }
    change();
    console.log(data);

    // 20
    ```
    ```javascript
    var data = 10;
    function change(){
    var data = 20; // var 사용하면 지역변수로 선언
    }
    change();
    console.log(data);

    // 10
    ```
- anonymous function : 익명함수
    - 선언과 동시에 호출
    - 전역함수로 사용할수 없도록 선언 > 외부에서 내부의 함수나 변수 사용 불가 > 보안
    ```javascript
    function minus1(n1, n2){
    console.log(n1 - n2);
    }
    minus1(1, 2);

    // -1
    ```
    ```javascript
    (function minus2(n1, n2){
    console.log(n1 - n2);
    }(2, 4));

    // -2
    ```
- return
    - 코드 실행 중단
    - 함수 코드 실행 결과를 출력 및 변수에 저장
    ```javascript
    function plus(n1, n2){
    return n1 + n2;
    }
    result = plus(1, 2);
    console.log(result);

    // 3
    ```
- Module Pattern : 모듈패턴
    - 모듈패턴을 이용한 객체생성
    ```javascript
    // Account 객체가 있으면 있는 객체 사용하고, 없으면 새로운 객체 생성
    var Account = Account || {};
    (function(_Account){

    var balance = 0;

    function getBalance(){
    return balance;
    }

    _Account.getBalance = function(){
    console.log('getter');
    return getBalance();
    }

    _Account.setBalance = function(money){
    console.log('setter', money);
    balance = money;
    }

    _Account.deposit = function(money){
    balance += money;
    }

    _Account.withdraw = function(money){
    balance -= money;
    }

    })(Account);

    // getter
    console.log(Account.getBalance());
    // getter
    // 0

    // setter
    Account.setBalance(10000);
    // setter 10000

    // getter
    console.log(Account.getBalance());
    // getter
    // 10000

    Account.withdraw(2000);
    // getter
    console.log(Account.getBalance());
    // getter
    // 8000
    ```
## 객체
- Array(배열), Class(클래스) 문법
- Array
    ```javascript
    // Arrary
    var data = [1, 2, 3, 'A', 'B'];
    console.log(typeof data, data);

    // object [ 1, 2, 3, 'A', 'B' ]
    ```
    ```javascript
    for(var i = 0; i < data.length; i++){
    console.log(i, data[i]);
    }
    // 0 1
    // 1 2
    // 2 3
    // 3 'A'
    // 4 'B

    // array.push() : 데이터 추가
    var data = [1, 2, 3, 'A', 'B'];
    data.push('C');
    console.log(data);
    // [ 1, 2, 3, 'A', 'B', 'C' ]
    ```
- Object : 객체
    ```javascript
    // 객체 생성 1
    var obj = { name: 'andy' };
    console.log(obj);
    // { name: 'andy' }

    // 객체 생성 2
    function Person(name) {
    this.name = name;
    }
    var person = new Person('andy');
    console.log(person);
    // Person { name: 'andy' }
    ```
    ```javascript
    // 객체의 변수 추가 및 수정
    var obj = {};
    obj.name = 'andy';
    obj['addr'] = 'seoul';
    console.log(obj);
    // { name: 'andy', addr: 'seoul' }

    // 데이터 읽어오기
    console.log(obj['name'], obj.addr);
    // andy seoul

    // 객체에 함수 저장
    var calc = {
        plus: function(n1, n2){
        return n1 + n2;
        }
    }
    console.log(calc.plus(1, 2));
    // 3

    // 객체의 변수(함수) 삭제
    var obj = {
        name: 'andy',
        addr: 'seoul'
    };
    console.log(obj);
    delete obj.addr;
    console.log(obj);
    // { name: 'andy', addr: 'seoul' }
    // { name: 'andy' }
    ```
- json object
    - 웹서비스에서 데이터를 주고 받을때 주로 사용하는 데이터 포멧
    ```javascript
    // 객체 > 문자열
    var obj = { name: 'andy', addr: 'seoul' };
    var json = JSON.stringify(obj);
    console.log(typeof obj, obj);
    console.log(typeof json, json);
    // object { name: 'andy', addr: 'seoul' }
    // string {"name":"andy","addr":"seoul"}

    // 문자열 > 객체
    var jsonObj = JSON.parse(json);
    console.log(typeof jsonObj, jsonObj);
    // object { name: 'andy', addr: 'seoul' }
    ```
- 웹브라우져 객체
    - window : 전역객체 : 모든 전역변수를 저장하는 객체
        ```javascript
        // window 객체
        var data = 10;
        var plus = function(n1, n2){
        return n1 + n2;
        }
        console.log(window.data);
        console.log(window.plus(1, 2));
        ```
    - location : url 데이터를 포함하는 객체
        ```javascript
        // location 객체
        location.href // 현재 페이지 URL
        location.origin // 현재 페이지 domain
        locaion.pathname // 현재 페이지 path
        location.prot // 현재 페이지 port
        ```
    - document : 페이지 문서에 대한 정보를 저장하는 객체
        ```javascript
        // documnet 객체
        document.title // 현재 페이지 title
        ```
- javascript를 이용한 element 선택
    - 아이디 : document.getElementById()
        ```html
        <input id="id-txt" type="text" value="mail_1">
        <script>
        var obj = document.getElementById("id-txt");
        console.log(obj.value);
        </script>
        ```
    - 클래스 : document.getElementByClassName()
        ```html
        <input class="class-txt" type="text" value="mail_2">
        <script>
        var obj = document.getElementsByClassName("class-txt");
        console.log(obj[0].value);
        </script>
        ```
    - 속성값 : document.getElementByName()
        ```html
        <input type="text" name="email" value="mail_3">
        <script>
        var obj = document.getElementsByName("email");
        console.log(obj[0].value);
        </script>
        ```
    - 태그 : document.getElementsByTagName()
        ```html
        <input type="text" name="email" value="mail_4">
        <script>
        var obj = document.getElementsByTagName("input");
        console.log(obj[3].value);
        </script>
        ```
    - 셀렉터 : document.querySelector()
        ```html
        <p class="txt">Data text</p>
        <script>
        var obj = document.querySelector(".txt");
        console.log(obj);
        </script>

        ```
- jQuery
    - javascript에서 어렵게 사용하는 웹브라우져 객체들을 쉽게 사용할수 있게 만들어주는 자바스크립트 라이브러리
- https://jquery.com/ (https://jquery.com/)
- 장점
    - 이벤트 핸들링이 편하다.
    - Dom 변경이 편하다.
    - Ajax 통신이 편하다.
- javascript event
```html
<button class="test-btn">Click</button>
<script>
 var obj = document.querySelector(".test-btn");
 obj.addEventListener("click", function(){
 alert("TEST");
 });
</script>

```
- jquery event
```html
<button class="test2-btn">Click</button>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
<script>
 $('.test2-btn').on("click", function(){
 alert("jQuery TEST");
 });
</script>
```
```html
<p class="data">Data</p>
<button class="test3-btn">Click</button>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
<script>
 $('.test3-btn').on("click", function(){
 $('.data').text("Science");
 });
</script>
```
```html
<p class="data2">Science</p>
<button class="test4-btn">Hide</button>
<button class="test5-btn">Show</button>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
<script>
 $('.test4-btn').on("click", function(){
 $('.data2').hide(1000);
 });
 $('.test5-btn').on("click", function(){
 $('.data2').show(1000);
 });
</script>
```
- Ajax(비동기) 통신으로 데이터 가져오기
    - 직방 사이트의 API로 활용하여 데이터 가져오기
```html
<input type="text" class="addr" value="논현동">
<button class="get-data">Info</button>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
 $('.get-data').on("click", function(){
 var addr = $('.addr').val();
 var url = 'https://apis.zigbang.com/v2/search?leaseYn=N&q=' + addr + '&serviceType=원룸';
 $.getJSON(url, function(result){
 console.log(result.items[0]);
 })
 });
</script>
```