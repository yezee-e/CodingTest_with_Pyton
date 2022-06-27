# 그래프 탐색 알고리즘:DFS/BFS   

탐색이란 많은 양의 데이터 중에서 **원하는 데이터를 찾는 과정**   
대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다      
코딩테스트에서 매우 자주 등장하는 유형으로 반드시 숙지필요   

### 🌟🌟**스택 자료구조**
* 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조   
* 입구와 출입구가 동일한 형태로 스태글 시각화   
EX) 펜케이크 쌓기   

```py
stack=[]

#삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력
print(stack) #최하단 원소부터 출력

#실행결과
# [1,3,2,5]
# [5,2,3,1]
```

### 🌟🌟**큐 자료구조**
* 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조   
* 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화    
EX) 줄서서 버스타기   

```py
from collections import deque

#큐 구현을 위해 deque라이브러리 사용
queue=deque()

#삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력

queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력

#실행결과
# deque([3,7,1,4])
# deque([4,1,7,3])
```

### 🌟🌟**재귀함수(recursive function)**   


재귀함수란 **자기 자신을 다시 호출하는 함수**를 의미   
단순한 형태의 재귀함수예제
* '재귀 함수를 호출합니다'라는 문자열을 무한히 출력
* 어느정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력
```py
   def recursive_function():
       print('재귀 함수를 호출합니다')
       recursive_function() #자기자신을 호출

    recursive_function()
```

* 재귀함수를 문제풀이에서 사용할 때는 재귀 함수의 종료 조거을 반드시 명시
* 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출

 ```py
    # 종료조건을 포함한 재귀함수예제

    def recursive_function(i):
        #100번째 호출을 했을때 종료되도록 종료조건 명시
        if i ==100:
            return 
        print(i,'번째 재귀함수에서', i+1,'번째 재귀함수를 호출합니다')
        recursive_function(i+1)
        print(i, '번째 재귀함수를 종료합니다')

    recursive_function(1)
    
```

### 🌟🌟**팩토리얼** 

* n! =1x2x3x...(n-1)xn 
* 수학적으로 0!과 1!의 값은 1입니다    
```py
#반복적으로 구현한 n!
def factorial_iterative(n):
    result =1
    #1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *=i
    return result

#재귀적으로 구현한 n!
def  factorial_recursive(n):
    if n <=1: # n이 1이하인 경우 1을 반환
        return 1
    # n! =n*(n-1)!을 그래도 코드로 작성하기
    return factorial_recursive(n-1)*n

#각자의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현:',factorial_iterative(5) ) #반복적으로 구현:120
print('재귀적으로 구현:',factorial_recursive(5) ) #재귀적으로 구현:120

```


### 🌟🌟**최대공약수 계산(유클리드 호제법)** 

* 두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있다
* 유클리드 호제법
    * 두 자연수 A,B에 대하여(A>B) A를 B로 나눈 나머지를 R이라고 합시다
    * 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다
* 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할 수 있다
    예시: GCD(192,162) ->GCD는 최대공약수를 의미   
<img src=pic\최대공약수.png width=50%></img> 

```py
def gcd(a,b):
    if a%b ==0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192,162))
```

* 재귀함수 사용의 유의사항
    + 재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성가능
    + 모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현
    + 재귀함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다
    + 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터의 메모리 내부의 스택 프레임에 쌓입니다
      (그래서 스택을 사용해야 할 때 구현상 **스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많음**)











