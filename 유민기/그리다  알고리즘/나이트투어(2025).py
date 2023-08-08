# 나이트 투어 2025
"""https://www.acmicpc.net/problem/2025"""
# 1. 체스판의 한 위치에서 시작한다.
# 2. knight의 현위치에서 knight가 이동할 수 있는 위치를 찾아서 좌표로 모두 표시한다.
# 3. knight가 이동 가능한 위치에서 다음 단계에서 knight가 이동할 수 있는 위치의 개수가 가장 적은 위치로 이동한다.
# 4. 모든 칸을 반복할 때까지 위 과정을 반복한다.
def knight_tour(n):
    # 체스판 초기화
    board = [[-1 for i in range(n)] for j in range(n)]
    # 나이트가 이동할 수 있는 방향
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    # 체스판의 한 위치에서 시작
    chess = (0, 0)
    board[chess[0]][chess[1]] = 0
    path = [chess]
    # 모든 칸을 방문할 때까지 반복
    for i in range(1, n*n):
        min_i = -1
        min = n+1
        c = []
        next_chess = ()
        for move in moves:
            nx = chess[0] + move[0]
            ny = chess[1] + move[1]
            if nx >= 0 and ny >= 0 and nx < n and ny < n and board[nx][ny] == -1:
                c_deg = get_degree(nx, ny, board, n)
                if c_deg < min:
                    min = c_deg
                    min_i = len(c)
                    next_chess = (nx, ny)
                c.append((nx, ny))
        if min_i == -1:
            return False
        board[next_chess[0]][next_chess[1]] = i
        chess = next_chess
        path.append(chess)
    return path

def get_degree(x, y, board, n):
    degree = 0
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if nx >= 0 and ny >= 0 and nx < n and ny < n and board[nx][ny] == -1:
            degree += 1
    return degree

# 예시: N=6인 경우
print(knight_tour(6))
