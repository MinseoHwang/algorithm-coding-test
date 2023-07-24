#안전역역(2468)
"""https://www.acmicpc.net/problem/2468"""

#이 문제는 (x,y)의 행과 열의 수를 n에 입력받고, n의 수에 따라 생성된 (x,y)좌표에서
#n의 값보다 낮은 수는 비에 잠겨서 안전하지 않은 지역으로 0으로 설정하고
#0이 아닌 나머지 지역을 각각 지역별로 탐색한다.
#1인 지역에서 출발하여 0이 나올때까지 반복하여 0이 나오면 값을 리턴하여 수를 카운트한다.
#1인 지역의 개수를 합하여 출력한다.
#======================================================================
#bfs로구현
from collections import deque

# 지역의 크기 N을 입력받습니다.
n = int(input())
graph = []  # 지역의 높이 정보를 저장할 리스트
result = []  # 장마철에 물에 잠기지 않는 안전한 영역의 개수를 저장할 리스트

# 지역의 높이 정보를 입력받습니다.
for _ in range(n):
    graph.append(list(map(int, input().split())))

# BFS를 사용하여 물에 잠기지 않는 영역을 탐색하는 함수를 정의합니다.
# (x, y) = 높이 정보를 저장한 2차원배열 x = 행, y = 열
# k = 물에 잠기는 높이
#visited = 방문 여부를 체크

# 물에 잠기지 않은 안전한 영역을 구하려면 어떻게 구해야할까?
#1. 처음에는 모든 지점의 방문 여부를 False로 초기화합니다.
#2. 특정 높이(height)보다 높은 지점에서 시작하여 BFS 탐색을 수행합니다.
#3. BFS 탐색 중, 방문한 지점은 visited 배열에 해당 위치를 True로 표시합니다.
#4. BFS 탐색을 마치면, visited 배열에서 True인 지점들은 물에 잠기지 않은 영역을 의미합니다.
def bfs(x, y, height, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((x, y))
    visited[x][y] = True
#q가 빌때까지 while문을 사용하여 반복한다.
    while q:
        x, y = q.popleft()
        #현재위치에서 4가지 방향으로 위치를 확인한다.
        for i in range(4):
            nx = x + dx[i] #nx = x의 다음 위치 행
            ny = y + dy[i] #ny = y의 다음 위치 열
            if 0 <= nx < n and 0 <= ny < n:
                # 물에 잠기지 않은 영역을 찾았을 경우, 해당 위치를 방문함을 True로 저장하고, 주변을 탐색합니다.
                if graph[nx][ny] > height and not visited[nx][ny]:
                    visited[nx][ny] = True #방문한지역 표시
                    q.append((nx, ny)) #다음 위치를 q에 추가한뒤 해당 위치에서 다시 bfs함수를 실행

# 높이는 1 이상 100 이하의 정수이므로 0부터 100까지 탐색합니다.
for height in range(101):
    count = 0  # 물에 잠기지 않는 안전한 영역의 개수를 세는 변수
    visited = [[False] * n for _ in range(n)]  # 방문 여부를 저장할 2차원 리스트

    # 모든 지점을 순회하면서 물에 잠기지 않은 영역을 탐색합니다.
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and not visited[i][j]:
                bfs(i, j, height, visited)
                count += 1
    result.append(count)  # 장마철의 높이 k에 대한 물에 잠기지 않는 안전한 영역의 개수를 저장합니다.

# 모든 장마철의 높이에 대한 결과 중에서 최대 값을 출력합니다.
print(max(result))


#======================================================================
# dfs로 구현
import sys

# 지역의 크기 N을 입력받습니다.
n = int(input())
graph = []  # 지역의 높이 정보를 저장할 리스트
result = []  # 장마철에 물에 잠기지 않는 안전한 영역의 개수를 저장할 리스트

# 지역의 높이 정보를 입력받습니다.
for _ in range(n):
    graph.append(list(map(int, input().split())))

# DFS를 사용하여 물에 잠기지 않는 영역을 탐색하는 함수를 정의합니다.
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    
    # 물에 잠기지 않은 영역을 찾았을 경우, 해당 위치를 방문했다고 표시하고 주변을 DFS로 탐색합니다.
    if graph[x][y] > height and not visited[x][y]:
        visited[x][y] = True
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True
    return False

for height in range(101):  # 높이는 1 이상 100 이하의 정수이므로 0부터 100까지 탐색합니다.
    count = 0  # 물에 잠기지 않는 안전한 영역의 개수를 세는 변수
    visited = [[False] * n for _ in range(n)]  # 방문 여부를 저장할 2차원 리스트

    # 모든 지점을 순회하면서 물에 잠기지 않은 영역을 탐색합니다.
    for i in range(n):
        for j in range(n):
            if dfs(i, j):  # dfs 함수를 호출하여 물에 잠기지 않은 영역을 찾고, 찾았으면 개수를 세어줍니다.
                count += 1
    result.append(count)  # 장마철의 높이 k에 대한 물에 잠기지 않는 안전한 영역의 개수를 저장합니다.

# 모든 장마철의 높이에 대한 결과 중에서 최대 값을 출력합니다.
print(max(result))
