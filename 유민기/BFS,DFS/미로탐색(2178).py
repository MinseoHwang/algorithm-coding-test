#미로 탐색(2178)
"""https://www.acmicpc.net/problem/2178"""

from collections import deque

#여기서 좌표값 (n,m)을 입력받는다. 이때, n,m은 (1,1)에서 출발한다고 문제에 정의가 되어있다.
#미로의 정보를 저장할 2차원 배열 graph를 생성할 것이다.
n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
"""graph = list(input())
    graph.append(graph)"""
#너비 우선 탐색을 사용하여 풀어보려 한다.
#bfs를 활용하기 위해서 먼저 이동할 네가지 방향(상,하,좌,우)를 정의한다. -> 반복문을 사용하기 위함
#미로에서 이동할 수 있는 칸 = 1
#미로에서 이동할 수 없는 칸 = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
q = [[0, 0]]
    #q가 빌때까지 while문을 사용하여 반복한다.
while q:
        x, y = q.pop(0)
        #현재위치에서 4가지 방향으로 위치를 확인한다.
        for i in range(4):
            nx = x + dx[i] #nx = x의 다음 위치 행
            ny = y + dy[i] #ny = y의 다음 위치 열
            # 다음 위치가 미로의 범위를 벗어날 경우 무시하고 다음 방향으로 진행한다.
            if 0 <= nx < n and 0 <= ny < m:
                """#if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            다음 위치에 벽이 있을 경우 무시하고 다음 방향으로 진행한다.
            if graph[nx][ny] == 0:
                continue"""
            #다음 위치가 이동가능한 칸이면 최단 거리를 갱신한뒤 q에 추가한다.
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1 # 최단 거리 갱신
                    q.append((nx, ny)) #다음 위치를 q에 추가한뒤 해당 위치에서 다시 bfs함수를 실행
"""(1,1)에서 출발하였으므로 (n,m)좌표에 각각 -1을 해서 값을 반환해준다.
return graph[n-1][m-1]"""
print(graph[n-1][m-1])
