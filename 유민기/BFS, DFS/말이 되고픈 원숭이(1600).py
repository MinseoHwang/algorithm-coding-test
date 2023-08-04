#말이 되고픈 원숭이 1600
"""https://www.acmicpc.net/problem/1600"""

# 3차원 배열을 만들어서 풀어야 할듯?
# visit[열[행][이동수]
# 이동 불가능한 경우에는 -1을 출력하면 될 것 같다.
# 원숭이가 이동할 수 있는 위치는 실제 체스에서 말이 이동하는 거리와 같다.
from collections import deque

K = int(input()) # 원숭이의 움직임 횟수를 k로 입력받는다.
m,n = map(int,input().split())  # m이 가로 n이 세로길이인 맵의 크기를 입력받는다.

# 상하좌우 배열 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 원숭이의 이동경로
mx = [-2, -1, 1, 2, 2, 1, -1, -2]
my = [1, 2, 2, 1, -1, -2, -2, -1]
# 원숭이의 위치와 움직임 횟수를 저장하는 3차원 배열을 초기화
visited = [[[0] * m for _ in range(n)] for _ in range(K+1)]
visited[0][0][0] = 1 # 원숭이가 시작 지점을 방문했다고 표시

maps = [] # 맵 정보를 저장할 리스트를 초기화
for i in range(n): #맵 정보 입력
    maps.append(list(map(int, input().split())))# 맵 정보를 입력받아 리스트에 저장
q = deque() # q 초기화
q.append([0,0,0,0]) # x = x좌표
                    # y = y좌표
                    # count = 이동비용(이것을 구하는 이유는 원숭이가 움직인 횟수의 최소값을 구하기 위함)
                    # action = 원숭이가 움직인 횟수

def bfs():  # x -> row, y -> col
    while q:
        x, y, count, action = q.popleft() # x, y 는 좌표 정보, count는 움직인 횟수, action은 원숭이의 움직임을 쓴 횟수
        if x == n - 1 and y == m - 1: # 목적지 도착
            print(count)
            return
        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if action >= K: # 원숭이의 움직임을 다 쓴 경우 visited에 최대 사용가능한 원숭이의 움직임 K로 저장한다.
                if 0 <= nx < n and 0 <= ny < m and visited[K][nx][ny] == 0 and maps[nx][ny] == 0:
                    visited[K][nx][ny] = 1
                    q.append((nx, ny, count + 1, action))
            else: # 원숭이의 움직임을 다 안 쓴 경우 현재 사용한 원숭이의 움직임을 visited에 저장
                if 0 <= nx < n and 0 <= ny < m and visited[action][nx][ny] == 0 and maps[nx][ny] == 0:
                    visited[action][nx][ny] = 1
                    q.append((nx, ny, count + 1, action))

        if action < K: # 아직 원숭이의 움직임을 사용하지 않은 경우
            for i in range(8):
                nx = x + mx[i]
                ny = y + my[i]
                if 0 <= nx < n and 0 <= ny < m and visited[action + 1][nx][ny] == 0 and maps[nx][ny] == 0: # 아직 방문하지 않았고, 이동 가능한 경우에 대해 방문표시를한다.
                    visited[action + 1][nx][ny] = 1
                    q.append((nx, ny, count + 1, action + 1))
    return -1 #큐를 다 돌렸는데 목적지 도착해서 return 되지 않은 경우 -1반환 (더이상 이동할 공간이 없는 것)

if bfs() == -1: # 최종결과가 -1이면 원숭이가 목적지에 도착하지 못했으므로 -1을 출력한다.
    print(-1)
