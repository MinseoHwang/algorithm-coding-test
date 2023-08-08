import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split()))
Hx, Hy = list(map(int, input().split()))
Ex, Ey = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    q.append([Hx - 1, Hy - 1, 1, 0]) 
    visited[Hx - 1][Hy - 1][1] = 1

    while q:
        x, y, magic, cost = q.popleft()

        if [x, y] == [Ex - 1, Ey - 1]:
            return cost
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny][magic]:
                    continue

                if magic and board[nx][ny]:
                    visited[nx][ny][0] = 1
                    q.append([nx, ny, 0, cost + 1])
                elif not board[nx][ny]:
                    visited[nx][ny][magic] = 1
                    q.append([nx, ny, magic, cost + 1])

    return -1

print(bfs())