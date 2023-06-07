# Sprint Challenge 32x

### 주의 사항
1. 여러분이 원하는 Tool과 reference를 사용할 수 있습니다. 

행운을 빕니다!

# Part 1

파이썬과 친숙해집니다.

## Part 1.1 - 필드

여러분은 커피 전문점 CodeBeans의 관리자입니다.
CodeBeans에서는 다양한 상품을 판매하고 있습니다.
여러분은 다양한 상품들을 좀더 나은 방법으로 정리하고 관리하는 방법을 고민하고 있습니다.

CodeBeans에서 판매하는 음료들은 모두 (`Product`)으로 간주되며,
음료들은 기본적으로 다음과 같은 필드(클래스 "내부"에 있는 변수)를 가집니다.

* 이름: `name` (문자열, 기본값: 없음)
* 가격: `price` (정수, 기본값: 30)
* 사이즈: `size` (정수, 기본값: 20)
* 따뜻함: `warmness` (실수, 기본값: 0.5)
* 달달함: `sweetness` (실수, 기본값: 0.5)
* 변수: `identifier` (정수, 기본값: 1000000 ~ 9999999 범위의 임의의 정수)

위 데이터를 모델링하기 위해 Python '클래스'를 작성합니다. 

위 내용과 같이 만든 클래스를 다음과 같이 Python repl에서 코드를 테스트할 수 있습니다.

```python
>>> from src.Part_1 import Product
>>> prod = Product('A Cold Drink')
>>> prod.name
'A Cold Drink'
>>> prod.price
30
>>> prod.size
20
>>> prod.warmness
0.5
>>> prod.sweetness
0.5
>>> prod.identifier
2812086  # 이 값은 실행에 따라 달라질 수 있습니다.
```

### Part 1.2 - 메소드

`Part 1.1`에서 작성한 코드가 정상적으로 수행되었나요?
위 예시와 같이 수행된다면 여러분은 훌륭한 코드를 작성해주신 겁니다!

하지만 이것만 가지고는 여러분이 할 수 있는 것은 아무 것도 없습니다.
메소드가 없기 때문입니다. 

따라서 두 개의 메소드를 추가해봅시다!

* `sellability(self)` (판매 가능성)
    * '사이즈(`size`)'를 '가격(`price`)'으로 나눈 값에 따라 다음 메시지를 반환합니다. 
    * `0.5` 보다 작을 경우: "Not so sellable..."
    * `0.5` 보다 크거나 같고, `1.0` 보다 작을 경우: "Kinda sellable."
    * `1.0` 을 크거나 같은 경우 : "Very sellable!"

* `calory(self)` (칼로리)
    * '사이즈(`size`)'와 '달달함(`sweetness`)'를 곱한 값에 따라 다음 메시지를 반환합니다. 
    * `10` 보다 작을 경우 "...it's light"
    * `10` 보다 크거나 같고, `50` 보다 작을 경우: "It's adequate."
    * 그 외의 경우 : "It's really heavy..!!"

코드를 저장하고 다음과 같이 테스트할 수 있습니다.

```python
>>> from src.Part_1 import Product
>>> prod = Product('A Warm Water')
>>> prod.sellability()
'Kinda sellable.'
>>> prod.calory()
"It's adequate."
```


### Part 1.3 - 상속
CodeBeans에서 판매하는 것은 일반적인 음료만 판매하는 것이 아닌
여러 종류의 음료(커피, 차 등)도 판매합니다.

다음을 수행하는 `Tea`라는 `Product`의 하위 클래스를 만듭니다.

* 기본값 변경
    * 사이즈(`size`) 기본값을 10으로 변경
    * 다른 기본값은 변경하지 않습니다.
* `calory` 메서드 재정의
    * 항상 `"...it's a tea. Only a few calories"`를 반환
* `drink` 메소드 추가
    * '따뜻함`warmness`' 값에 따라 다음 메시지를 반환합니다.
    * 0.5 미만이면 : "it's too cold..."
    * 0.5 보다 크거나 같고, 1.0 보다 작은 경우 : "Oh, it's warm!"
    * 1.0 보다 크거나 같은 경우 : "It's too hot!!"


테스트 실행 예 :
```python
>>> from src.Part_1 import Tea
>>> tea = Tea('Green Tea')
>>> tea.price
30
>>> tea.size
10
>>> tea.drink()
"Oh, it's warm..!"
>>> tea.calory()
"...it's a tea. Only a few calories"
```


# Part 2
## 2.1 **get_results** 함수를 만듭니다.

> 함수는 아래의 코드에 있는 body를 활용하여 `(utc_datetime, value)`로 이루어진 tuple들의 리스트를 반환해야합니다.

 ```python
_, body = api.measurements(city='Los Angeles', parameter='pm25')
 ```

- Hint: 다음의 링크를 들어가면 `body`에 들어가는 정보를 확인 할 수 있습니다 (https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25)
- 필요한 datetime과 value는 중첩 된 dictionary 안에 있습니다, 어떻게 필요한 데이터를 빼올 수 있을지 여러가지 시도를 해보시길 바랍니다.

## 2.2 **MongoDB** 에 데이터를 입력합니다.

> src/Part_2.py 의 1.2 MONGODB SETUP 을 수정합니다. 

- 자신의 MongoDB 연결정보를 입력합니다.
- COLLECTION_NAME 은 유지합니다.
- MongoDB 에 OpenAQ 에서 받은 body가 입력되어 있어야합니다.
