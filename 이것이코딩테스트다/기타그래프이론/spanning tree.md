# 신장트리
* 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분그래프를 의미
    * 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도함       
            <img src=etc_pic/신장트리.png width=70%></img>    

### 🌟🌟**최소신장트리**
* 최소한의 비용으로 구성되는 신창트리를 찾아야할때 어떻게 해야할까?
* 예로 N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치해야하는 경우
    * 두 도시 A,B를 선택했을때 A에서 B로 이동하는 경로가 반드시 존재하도록 도로를 설치     
            <img src=etc_pic/최소신장트리찾기.png width=70%></img>    


### 🌟🌟**크루스칼 알고리즘**
* 대표적인 최소 신장 트리 알고리즘
* 그리디 알고리즘으로 분류
* 동작과정
    1. 간선 데이터의 비용에 따라 오름차순으로 정렬
    2. 간선 데이터를 비용에 따라 오름차순으로 정렬
        * 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
        * 사이클이 발생하는 경우 최소 신장트리에 포함시키지 않는다
    3. 모든 간선에 대하여 2번의 과정 반복   
            <img src=etc_pic/신장1.png width=70%></img>    
            <img src=etc_pic/신장2.png width=70%></img>    
            <img src=etc_pic/신장3.png width=70%></img>    
            <img src=etc_pic/신장4.png width=70%></img>    
            <img src=etc_pic/신장5.png width=70%></img>    
            <img src=etc_pic/신장6.png width=70%></img>    
            <img src=etc_pic/신장7.png width=70%></img>    
            <img src=etc_pic/신장8.png width=70%></img>    
            <img src=etc_pic/신장9.png width=70%></img>    
            <img src=etc_pic/신장10.png width=70%></img>    
            <img src=etc_pic/신장11.png width=70%></img>    

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

#모든 간선을 담을 리스트와, 최종 비용을 담을 함수
edges=[]
result=0

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

#모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost=map(int, input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()
#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b=edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result +=cost
print(result)

```
* 성능분석
    * 간선의 개수가 E개일 때, O(ElogE)의 시간복잡도를 가진다
    * 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선의 정렬을 수행하는 부분

