from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))

def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board[nx][ny] == 0:
                continue

            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

    return board[n - 1][m - 1]

print(bfs())