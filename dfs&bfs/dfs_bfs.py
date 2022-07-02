#DFS소스코드 예제
#각 노드가 연결된 정보를 표현
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

#각 노드가 방문된 정보를 표현
visited=[False]*9

#dfs메서드 정의
def dfs(graph,v,visited):
    #현재노드를방문처리
    visited[v]=True
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#정의된 dfs 함수 호출
dfs(graph,1,visited)






#BFS소스코드 예제
from collections import deque

#각 노드가 연결된 정보를 표현
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
#각 노드가 방문된 정보를 표현
visited=[False]*9

#dfs메서드정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque라이브러리사용
    queue=deque([start])
    #현재노드를방문처리
    visited[start]=True
    #큐가 빌때까지반복
    while queue:
        #큐에서 하나씩 원소를 뽑아 출력
        v=queue.popleft() #선출하기
        print(v,end=' ')
        #아직 방문하지 않은 인접한 원소들을 큐에삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

#정의된 dfs 함수 호출
bfs(graph,1,visited)
