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


def dfs(v):
    visited[v] = 1
    for i in range(1,n+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

dfs(1)
print(sum(visited)-1)