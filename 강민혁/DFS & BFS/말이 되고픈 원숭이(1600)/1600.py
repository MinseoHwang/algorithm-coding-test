from collections import deque

# 입력값
k = int(input())
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우, 체스 나이트 이동
dist = [[1,0],[0,1],[-1,0],[0,-1]]
horse = [[-2,-1], [-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,-2],[1,2]]

def bfs():
  visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
  queue = deque()
  queue.append([0,0,0])
  visited[0][0][0] = 1

  while queue:
    x, y, z = queue.popleft()

    # 목표 지점에 도달하면 return
    if x==n-1 and y==m-1:
      return visited[x][y][z]-1

    # 상하좌우로 이동하는 경우
    for (i,j) in dist:
      dx, dy = x+i, y+j
      # dx,dy가 0과 같거나 n보다 작을때 (맵 안에 있을 때)
      # 방문한 적 없을 때 ( 한번 지나간 곳은 지나가지 않는다)
      # graph[dx][dy]가 0이 아닐 때 (장애물이 있는 곳이 아니라 갈 수 있는 상황)
      if 0<=dx<n and 0<=dy<m and not visited[dx][dy][z] and not graph[dx][dy]:
        visited[dx][dy][z] = visited[x][y][z]+1     # 한번 움직였다는 것 표시
        queue.append([dx,dy,z])

    # 말 이동 수보다 작을 경우에만 이동
    if z<k:
      for (hi, hj) in horse:
        hx, hy = x+hi, y+hj
        if 0<=hx<n and 0<=hy<m:     # 격자판 안 범위
          if not graph[hx][hy]:     # 장애물이 아닐 때
            # z+1번째 말처럼 이동하는 중
            if not visited[hx][hy][z+1]:
              visited[hx][hy][z+1] = visited[x][y][z]+1
              queue.append([hx,hy,z+1])

  return -1

# 정답 출력
print(bfs())