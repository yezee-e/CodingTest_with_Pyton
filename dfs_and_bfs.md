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
    # n! =n*(n-1)!을 그대로 코드로 작성하기
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



### 🚀**DFS(Depth-First Search)**
* DFS는 깊이 우선 탐샘이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
* DFS는 **스택자료구조(혹은 재귀함수)**를 이용

* 구체적인 동작과정    
    **++** 탐색 시작 노드를 스택에 삽입하고 방문처리   

    **++** 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리   
        (방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다)   

    **++** 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

* DFS 동작예시   
    [step 0] 
    :그래프를 준비합니다(방문기준-번호가 낮은 인접 노드부터)   
    시작노드:1   

    [step 1] 
    : 시작노드인 '1'을 스택에 삽입하고 방문 처리      
            <img src=pic\step1.png width=55%></img>     

    [step 2] 
    :스택의 최상단 노드인 '1'에 방문하지 않은 인접노드 '2', '3', '8'이 있다    
    이중에서 가장 작은 노드인 '2'를 스택에 넣고 방문처리    
            <img src=pic\step2.png width=55%></img> 

    [step 3] 
    :스택의 최상단 노드인 '2'에 방문하지 않은 인접노드 '7'이 있다  
    따라서 '7'번 노드를 스택에 넣고 방문처리    
        <img src=pic\step3.png width=55%></img> 

    [step 4]   
    :스택의 최상단 노드인 '7'에 방문하지 않은 인접노드 '6','8'이 있다   
    이중에서 가장 작은 노드인 '6'을 스택에 넣고 방문처리  
        <img src=pic\step4.png width=55%></img> 

    [step 5]   
    :스택의 최상단 노드인 '6'에 방분하지 않은 인접 노드가 없습니다   
    따라서 스택에서 '6'번 노드를 꺼냅니다   
    <img src=pic\step5.png width=55%></img> 

    [step 6]   
    :스택의 최상단 노드인 '7'에 방문하지 않은 인접 노드 '8'이 있다   
    따라서 '8'번 노드를 스택에 넣고 방문처리   
        <img src=pic\step6.png width=55%></img> 

    -> 이러한 과정을 반복했을때 **전체 노드의 탐색 순서**(스택에 들어간 순서)는 다음과 같다
         <img src=pic\step동작예시.png width=55%></img>    

* DFS소스코드 예제
```py
#각 노드가 연결된 정보를 표현(2차원 리스트)
#노드가 1번 부터 시작하는 경우가 많지만 인덱스 0을 만들어 비워둠
#인접 리스트 방식으로 그래프를 표현
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현(1차원 리스트)
#기본적으로 False값으로 초기화(방문하지 않은 노드)
visited=[False]*9

#dfs 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v]=True
    print(v,end='')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


#정의된 DFS함수 호출
dfs(graph, 1, visited) #1 2 7 6 8 3 4 5

```

### 🚀**BFS(Breadth-First Search)**
* 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘   
* **큐 자료구조**를 이용   
* 구체적인 동작과정   
    **++** 탐색 시작 노드를 큐에 삽입하고 방문처리   
    **++** 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리   
    **++** 더 이상 2번의 과정을 수행할 수 없을때까지 반복   

* BFS 동작예시   
    [step 0] 
    :그래프를 준비합니다(방문기준-번호가 낮은 인접 노드부터)   
    시작노드:1   

    [step 1] 
    : 시작노드인 '1'을 큐에 삽입하고 방문 처리      
            <img src=pic\step1.png width=55%></img>     

    [step 2] 
    :큐에서 노드 '1'을 꺼내 방문하지 않은 인접 노드 '2', '3', '8'을 큐에 삽입하고 방문처리    
            <img src=pic\큐2.png width=55%></img> 

    [step 3] 
    :큐에서 노드 '2'를 꺼내 방문하지 않은 인접 노드 '7'을 큐에 삽입하고 방문처리   
        <img src=pic\큐3.png width=55%></img> 

    [step 4]   
    :큐에서 노드 '3'을 꺼내 방문하지 않은 인접노드 '4', '5'를 큐에 삽입하고 방문처리  
        <img src=pic\큐4.png width=55%></img> 

    [step 5]   
    :큐에서 노드 '8'을 꺼내고 방문하지 않은 인접 노드가 없으므로 무시   
    <img src=pic\큐5.png width=55%></img> 

  

    -> 이러한 과정을 반복했을때 **전체 노드의 탐색 순서**(큐에 들어간 순서)는    
    다음과 같다   
         <img src=pic\bfs동작예시.png width=55%></img>   


* BFS 소스코드 예제
```py
from collections import deque

#각 노드가 연결된 정보를 표현(2차원 리스트)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
] 

#각 노드가 방문된 정보를 표현(1차원 리스트)
visited=[False]*9

#bfs 메서드 정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque라이브러리 사용
    queue=deque([start])
    #현재 노드를 방문처리
    visited[start]=True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 히나의 원소를 뽑아 출력하기
        v=queue.popleft() #popleft()먼저 들어간 원소 꺼내기
        print(v, end='')
        #아직 빙문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

#정의된 bfs함수 호출
bfs(graph, 1, visited) #1 2 3 8 7 4 5 6







