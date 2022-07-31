# 서로소집합(Disjoint Sets)
공통원소가 없는 두 집합   
            <img src=etc_pic/서로소.jpeg width=70%></img>    

<br/> 

서로소 집합 자료구조   
* 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
* 서로소 집합 자료구조넌 두 종류위 연산을 지원
    * 합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
    * 찾기(Find); 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
* 서로소 집합 자료구조는 합치기 찾기(Union Find)자료구조라고도 불림

* 여러개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같다    
    1. 합집합연산을 확인하여 서로 연결된 두 노드 A,B를 확인    
        1)A와B의 루트 노드 A*,B*를 각각 찾습니다      
        2)A*를 B*의 부모노드로 설정
    2. 모든 합집합 연산을 처리할때 까지 1번 과정을 반복    
* 동작과정 살펴보기   
            <img src=etc_pic/서로소.jpeg width=70%></img>    
            <img src=etc_pic/서로소2.jpeg width=70%></img>     
            <img src=etc_pic/서로소3.jpeg width=70%></img>    
            <img src=etc_pic/서로소4.jpeg width=70%></img>    
            <img src=etc_pic/서로소5.jpeg width=70%></img>   
* 연결성  
    기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없다        
    루트 노드를 찾기 위해 부모 테이블을 계속해서 확인하며 거슬러 올라가야 한다         
            <img src=etc_pic/서로소6.jpeg width=70%></img>    
    아래 예시에서 노드3의 로트를 찾기 위해서는 노드2를 거쳐 노드1에 접근해야 한다    
            <img src=etc_pic/서로소연결성.jpeg width=70%></img>   


* 기본적인 구현방법(python)
```py
#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x]!=x:
        return find_parent(parent, parent[x])
    return x

#두 원소가 속한 집합을 합치기 
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드의 개수와 간선(union 연산)의 개수 입력받기
v,e=map(int, input().split())
parent=[0]* (v+1) #부모 테이블 초기화하기

#부모 테이블상에서, 부모자기 자신으로 초기화
for i in range(1, v+1):
    parent[i]=i

#union 연산을 각각 수행
for i in range(e):
    a,b=map(int, input().split())
    union_parent(parent,a,b)

#각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합:',end='')
for i in range(1, v+1):
    print(parent[i], end='')

print()

#부모 테이블 내용 출력하기
print("부모테이블:",end='')
for i in range(1, v+1):
    print(parent[i], end='')
```

* 기본적인 구현 방법의 문제점
    * 합집합 연산이 편향되게 이루어지는 경우 찾기 함수가 비효율적으로 동작
    * 최악의 경우네는 찾기 함수가 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V)   
            <img src=etc_pic/서로소문제점.jpeg width=70%></img>    

<br/>

### 🌟🌟**서로집합자료구조:경로압축**
* 찾기 함수를 최적화하기 위한 방법으로 경로압축을 이용
    * 찾기 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신
    ```py
    # 특정 원소가 속한 집합 찾기
    def find_parent(parent, x):
        #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x]!=x:
            parent[x]=find_parent(parent,parent[x])
        return parent[x]
    ```

* 경로압축기법을 적용하면 각 노드에 대하여 찾기 함수를 호출한 이후에 해당 노드의 루트 노드가 바로 부모녿가 된다    
* 동일한 예시에 대해서 모든 합집합함수를 처리한 후 각 원소에 대하여 찾기 함수를 수행하면 다음과 같이 부모 테이블이 갱신
* 기본적인 방법에 비하여 시간 복잡도가 개선   

* 경로압축(python)
```py
#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x]!=x:
        parent[x]= find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기 
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드의 개수와 간선(union 연산)의 개수 입력받기
v,e=map(int, input().split())
parent=[0]* (v+1) #부모 테이블 초기화하기

#부모 테이블상에서, 부모자기 자신으로 초기화
for i in range(1, v+1):
    parent[i]=i

#union 연산을 각각 수행
for i in range(e):
    a,b=map(int, input().split())
    union_parent(parent,a,b)

#각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합:',end='')
for i in range(1, v+1):
    print(parent[i], end='')

print()

#부모 테이블 내용 출력하기
print("부모테이블:",end='')
for i in range(1, v+1):
    print(parent[i], end='')
```
### 🌟🌟**서로집합자료구조:사이클판별**
* 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용
    * 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별
* 사이클 판별알고리즘은 다음과 같다
    1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인
        * 루트 노드가 서로 다르다면 두 노드에 대하여 합집합연산을 수행
        * 루트 노드가 서로 같다면 사이클이 발생한 것
    2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복

* 동작과정   
            <img src=etc_pic/사이클1.jpeg width=70%></img>    
            <img src=etc_pic/사이클2.jpeg width=70%></img>    
            <img src=etc_pic/사이클3.jpeg width=70%></img>    
            <img src=etc_pic/사이클4.jpeg width=70%></img>   

* 서로소집합을 활용한 사이클 판별
```py
#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드를 찾을때까지 재귀호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드의 개수와 간선이 개수 입력받기
v,e=map(int, input().split())
parent=[0]*(v+1) #부모테이블 초기화하기

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i
    
cycle=False #싸이클 발생 여부

for i in range(e):
    a,b=map(int, input().split())
    #사이클이 발생한 경우 종료
    if find_parent(parent,a) ==find_parent(parent,b):
        cycle=True
        break
    #사이클이 발생하지 않았다면 합집합 연산 수행
    else:
        union_parent(parnet,a,b)

if  cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클이 발생하지 않았습니다")
``` 
