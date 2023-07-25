import sys
from collections import deque
n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True # 1번 컴퓨터부터 시작
queue = deque([1]) # 1번 컴퓨터부터 시작

while queue:
    c = queue.popleft()
    for i in graph[c]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = True

print(sum(visited) - 1) # 1번 컴퓨터 제외
    
