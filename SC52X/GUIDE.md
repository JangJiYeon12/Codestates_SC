# Sprint Challenge: Data Structures and Algorithms

## 1번 문제 - 재귀함수 (총 문제 : 3개)

- 각 문제의 요구사항을 파악하여 재귀함수로 문제를 해결해본다.
- 단 문제를 해결하면서 매개변수는 수정하지 않는다.

### addNumber

- `num`을 입력받아 1부터 num까지의 총 합을 반환하는 함수를 작성한다.
- 단 `num`에는 1이상의 정수만 들어간다.

입력
```
10
```

출력
```
55
```

### countDown

- `num`을 입력받아 `num`부터 1까지 숫자를 리스트에 넣고 마지막에 `'발사!!'`를 포함한 리스트를 반환하는 함수를 작성한다.
- 단 `num`에는 1이상의 정수만 들어간다.

입력
```
10, []
```

출력
```
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, '발사!!']
```

### printStar

- `num`을 입력받아 1개에서 num개의 별을 차례대로 포함한 리스트를 반환하는 함수를 작성한다.
- 단 `num`에는 1이상의 정수만 들어간다.

입력
```
5
```

출력
```
['*', '**', '***', '****', '*****']
```

---

## 2번 문제 - 내림차순 정렬 (총 문제 : 3개)

- 매개변수로 리스트를 받아 내림차순으로 정렬된 리스트를 반환하는 함수를 작성한다.

- 선택정렬과 버블정렬, 삽입 정렬의 개념을 사용하여 코드를 작성한다. 

- 단, 매개변수로 들어온 리스트를 내림차순으로 정렬하는 것이 아닌, 정렬된 리스트를 반환하는 함수를 작성한다.

---

## 3번 문제 - 🔥 도전과제

- 문제해결를 해결하기 위해 다양한 개념을 적용해본다.

  - 조건 : 2개의 문장을 입력받고, 두 문장을 비교하여 '입력받은 두 번째 문장에 추가된 단어'를 찾는 코드를 구현한다.
  - 단어는 공백을 기준으로 구분된다. 공백이 2개 이상 같이 있는 경우는 고려하지 않는다.
  - 참조개념 : 딕셔너리의 키에 따른 값 개념
  
- 예시입출력값

```
    1) 정상적으로 반환되는 경우
    첫번째 문장입력 : the best
    두번째 문장입력 : the best is
    추가된 단어 :  is

    2) 첫번째 문장에 추가된 단어는 알 수 없다.('None' 은 알 수 없음을 의미)
    첫번째 문장입력 : the best is
    두번째 문장입력 : the best
    추가된 단어 :  None
```