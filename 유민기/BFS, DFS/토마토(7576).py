#토마토 7576
"""https://www.acmicpc.net/problem/7576"""
#너비 우선 탐색을 사용하여 풀어보려 한다.
#bfs를 활용하기 위해서 먼저 이동할 네가지 방향(상,하,좌,우)를 정의한다. -> 반복문을 사용하기 위함
# -1 = 토마토가 들어있지 않은 칸(벽)
# 0 = 토마토가 익지 않은 칸
from collections import deque

#좌표값 (n,m)을 입력받는다.
#미로의 정보를 저장할 2차원 배열 graph를 생성할 것이다.
m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 1 = 토마토가 익은 칸
q = deque([]) # 처음부터 익어있는 토마토
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n): # 모든 좌표를 순회하면서 초기 익어있는 토마토들의 좌표를 큐에 추가합니다.
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])
while q: # BFS
    x, y = q.popleft()
    for i in range(4): # 상하좌우 방향에 대해서 인접한 칸을 검사합니다.
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0: # 인접한 칸이 미로 내부에 있고, 익지 않은 토마토라면 토마토를 익힙니다.
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx,ny])

total = 0 # 모든 토마토가 익었는지 검사하기 위해 결과값을 저장할 변수 total을 초기화합니다.
for i in graph: # 모든 칸을 순회하면서, 익지 않은 토마토가 있는지 확인하고, 최소 익히는 날짜를 구합니다.
    for j in i:
        if j == 0:
            print(-1) #벽에 막혀 토마토를 익히지 못했다면 -1 출력
            exit(0) #프로그램을 종료
    total = max(total, max(i)) #토마토를 다익혔으면 결과를 total에 저장
print(total - 1) # 시작을 1로 표현했으므로 1을 빼줘서 최종 결과를 출력합니다.


# 다른 사람이 작성한 코드
"""
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
l = []
mature = deque()
for y in range(N):
    l.append(list(map(int, input().split())))
    for x in range(M):
        if l[y][x] == 1:
            mature.append((x, y))

while mature:
    x, y = mature.popleft()
    for p in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
        x2, y2 = p
        if 0 <= x2 < M and 0 <= y2 < N and l[y2][x2] == 0:
            l[y2][x2] = l[y][x] + 1
            mature.append(p)

print(-1 if any(0 in l2 for l2 in l) else max(map(max, l)) - 1)"""