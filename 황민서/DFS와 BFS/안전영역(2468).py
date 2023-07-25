from collections import deque

n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

max_depth = 0
for i in range(n):
    for j in range(n):
        if max_depth < board[i][j]:
            max_depth = board[i][j]

def bfs(y, x, depth, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if board[ny][nx] > depth and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append((ny, nx))
    

max_cnt = 1

for k in range(max_depth):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > k and visited[i][j] == False:
                cnt += 1
                bfs(i, j, k, visited)
    if max_cnt < cnt:
        max_cnt = cnt
    

print(max_cnt)