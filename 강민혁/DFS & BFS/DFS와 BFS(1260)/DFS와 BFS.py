from collections import deque

#입력
N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N+1) #dfs의 방문기록
visited2 = [False] * (N+1) #bfs의 방문기록

def bfs(V):
    q = deque([V])      # deque 초기화 방법 : 변수 = deque([value, value, value])
    visited2[V] = True
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in range(1, N+1): # 1부터 N까지 돈다
            if not visited2[i] and graph[V][i]:    # 만약 해당 i값을 방문하지 않았고 v와 연결이 되어 있다면
                q.append(i) # 그 i 값을 추가
                visited2[i] = True # i 값을 방문처리

def dfs(V):
    visited1[V] = True #해당 V값 방문처리
    print(V, end=" ")
    for i in range(1,N+1):
        if not visited1[i] and graph[V][i]: # 만약 i 값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i) # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)



dfs(V)
print()
bfs(V)



'''
예제 입력
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력
1 2 4 3
1 2 3 4

'''