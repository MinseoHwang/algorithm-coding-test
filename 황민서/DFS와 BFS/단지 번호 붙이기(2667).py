# 입력
from collections import deque

n = int(input())

board = [list(map(int, input())) for _ in range(n)]
result = []

dx = [0, 0, 1, -1] # 이동할 때 쓰는 좌표값
dy = [1, -1, 0, 0] # 이동할 때 쓰는 좌표값

# 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    board[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 보드 범위 밖으로 나가면 다음으로 넘김
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    result.append(cnt)
    
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bfs(i, j)

# 출력
result.sort(key=lambda x: x)

print(len(result))
for i in range(len(result)):
    print(result[i])
