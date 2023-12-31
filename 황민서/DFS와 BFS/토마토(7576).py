from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))



def bfs():
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x

            if 0 > ny or n <= ny or 0 > nx or m <= nx:
                continue
            
            if board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                queue.append((ny, nx))

queue = deque()

for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                 queue.append((i, j))

bfs()

max_cnt = 0
for i in range(n):
     for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit(0)
     max_cnt = max(max(board[i]), max_cnt)

print(max_cnt - 1)
        