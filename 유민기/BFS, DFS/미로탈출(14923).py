#너무 어려워서 clone coding했음.

import sys
from collections import deque


def find_min_path(arr, start, end):

    que = deque()
    r = len(arr)
    c = len(arr[0])
    # visited[r][c][a]  a = 0 이면 지팡이 안쓴것, 1이면 지팡이 쓴것
    visited = [[[0] * 2 for _ in range(0, c)] for _ in range(0, r)]
    start_row, start_col = start
    end_row, end_col = end
    # 1부터 시작
    visited[start_row][start_col][0] = 1
    que.append((start_row, start_col, False))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while que:
        row, col, is_use = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]
            
            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                continue
            # 벽
            if arr[next_row][next_col]:
                # 이미 썼으면 pass
                if is_use:
                    continue
                # 딱 한번 부술 수 있다.
                visited[next_row][next_col][1] = visited[row][col][0]+1
                que.append((next_row, next_col, True))
            else:
                if is_use:
                    if visited[next_row][next_col][1]:
                        continue
                    if next_row == end_row and next_col == end_col:
                        # 1부터 시작했으므로 결과도 1줄여줘야함
                        return visited[row][col][1]
                    visited[next_row][next_col][1] = visited[row][col][1]+1
                else:
                    if visited[next_row][next_col][0]:
                        continue
                    if next_row == end_row and next_col == end_col:
                        return visited[row][col][0]
                    visited[next_row][next_col][0] = visited[row][col][0]+1
                que.append((next_row, next_col, is_use))
    return -1
    

N, M = map(int, sys.stdin.readline().split())
Hx, Hy = map(int, sys.stdin.readline().split())
Ex, Ey = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

# 주어진 좌표와 인덱스 1차이나는거 미리 가공
answer = find_min_path(MAP, (Hx-1, Hy-1), (Ex-1, Ey-1))
print(answer)
