from collections import deque

#입력
n = int(input())
v = int(input())

# 연결상태와 방문한 컴퓨터를 위한 코드
graph = [[0]* (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(v):  # 연결 상태
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


visited[1] = 1 # 1번 컴퓨터로부터 감염이 시작된다.
q = deque([1])

while q:
    c = q.popleft()

    for i in range(1, n+1):
        if not visited[i] and graph[c][i]:
            q.append(i)
            visited[i] = 1

print(sum(visited)-1)
