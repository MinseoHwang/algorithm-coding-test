from collections import deque
#입력
n, m, v = list(map(int, input().split()))

graph = [[0]*(n+1) for i in range(n+1)]


visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

for i in range(m):
  a,b=map(int,input().split())
  graph[a][b]=graph[b][a]=True

#구현
def dfs(v):
  visited_dfs[v]=1
  print(v,end=' ')
  for i in range(1, n+1):
    if(visited_dfs[i]==0 and graph[v][i]==1):
      dfs(i)

def bfs(v):
  queue=deque([v]) # deque는 스택과 큐의 기능을 모두 가지고 있는 객체로, 양방향에서 삽입과 삭제가 일어날 수 있는 자료구조이다
  visited_bfs[v]=1
  
  while queue:
    v=queue.popleft()
    print(v, end=' ')
    for i in range(1, n+1):
      if(visited_bfs[i]==0 and graph[v][i]==1):
        queue.append(i)
        visited_bfs[i]=1

dfs(v)
print()
bfs(v)