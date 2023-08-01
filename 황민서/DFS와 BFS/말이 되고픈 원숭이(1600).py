import sys
from collections import deque
input = sys.stdin.readline

k = int(input()) 
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs():
    q = deque()
    visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]

    q.append([0, 0, k, 0]) 
    visited[0][0][k] = 1

    while q:
        y, x, horse, cost = q.popleft()

        if [y, x] == [h - 1, w - 1]:
            return cost
        
        if horse > 0:
            for i in range(8):
                ny, nx = y + hy[i], x + hx[i]
                if 0 <= ny < h and 0 <= nx < w:
                    if visited[ny][nx][horse]:
                        continue
                    if horse and board[ny][nx]:
                        visited[ny][nx][horse-1] = 1
                        q.append([ny, nx, horse-1, cost + 1])
                    elif not board[ny][nx]:
                        visited[ny][nx][horse] = 1
                        q.append([ny, nx, horse-1, cost + 1])
            
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if visited[ny][nx][horse]:
                    continue

                if horse and board[ny][nx]:
                    visited[ny][nx][horse-1] = 1
                    q.append([ny, nx, 0, cost + 1])
                elif not board[ny][nx]:
                    visited[ny][nx][horse] = 1
                    q.append([ny, nx, horse, cost + 1])

    return -1

print(bfs())