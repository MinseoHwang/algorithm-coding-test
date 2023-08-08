
from collections import deque

# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
N,M,V = map(eval,input().split())

# 연결 그래프 생성
graph = [[False] * (N+1) for _ in range(N+1)]

# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 입력으로 주어지는 간선은 양방향이다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다
for _ in range(M):
    a,b = map(eval, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N+1) #DFS 방문기록
visited2 = [False] * (N+1) #BFS 방문기록

#방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문

# DFS 재귀
def DFS_rec(V):
    visited1[V] = True  #해당 정점 V 방문처리
    print(V, end=' ')
    # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
    for i in range(1, N+1): #i=1,2,...,N
        if not visited1[i] and graph[V][i]: #만약 정점 i를 방문하지 않았고 정점 V와 연결되어 있다면
            DFS_rec(i)  # 정점 i를 이용해서 DFS(i) 호출 ( 깊이 우선 탐색 )

# DFS 스택 LIFO
def DFS_stack(V):
    s = deque([V])  #시간 복잡도가 낮은 deque 사용
    while s:        # s이 빌때 까지
        V = s.pop() #deque 의 제일 뒤의 값 꺼낸다.
        if not visited1[V]:
            print(V, end=' ')
            visited1[V] = True  # 해당 정점 V 방문처리
        # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
        for i in range(N,0,-1):    #i=N,N-1,...,1
            if not visited1[i] and graph[V][i]: #만약 정점 i를 방문하지 않았고 정점 V와 연결되어 있다면
                s.append(i)         #정점 i 추가
                #visited1[i] = True  #정점 i 방문 처리

# BFS 큐 FIFO
def BFS(V):
    q = deque([V]) #시간 복잡도가 낮은 deque 사용
    while q:            #q가 빌때까지
        V = q.popleft() #deque 의 첫번째 값 꺼낸다.
        if not visited2[V]:
            print(V, end=' ')
            visited2[V] = True  # 해당 정점 V 방문처리
        # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
        for i in range(1, N+1): #i=1,2,...,N
            if not visited2[i] and graph[V][i]: #만약 정점 i를 방문하지 않았고 정점 V와 연결되어 있다면
                q.append(i)     #정점 i 추가



DFS_rec(V)
#DFS_stack(V)
print()
BFS(V)


"""
deque를 사용하는 이유는?
list의 pop 보다 시간복잡도가 낮은 deque의 popleft 사용하기 위해서
4 5 1
1 2
1 3
1 4
2 4
3 4



1
|______
|  |  |
2  3__4
|_____|

"""
