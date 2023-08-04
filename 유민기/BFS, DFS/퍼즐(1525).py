# 퍼즐 1525
"""https://www.acmicpc.net/problem/1525"""
# 이 문제를 풀기위해선 3x3 2차원 배열을 1차원 배열이라고 생각하고 123456780으로 정렬 시키는 방법으로 풀이하는 것이 좋다.
from collections import deque

puzzle = "" # 빈 문자열 puzzle를 초기화합니다.

for _ in range(3):# 사용자로부터 3줄로 이루어진 8 퍼즐의 초기 상태를 입력받습니다.
    puzzle += input()
puzzle = puzzle.replace(" ", "")# 입력받은 문자열에서 공백을 모두 제거합니다.
                                # 입력 예시: "1 2 3 4 5 6 7 8 0" -> "123456780"
p = '123456780'# 목표로 하는 정답 상태를 나타내는 문자열 p를 설정합니다.
                # '123456780'은 각 숫자가 1부터 8까지 순서대로 나열되어 있는 상태를 나타냅니다.
visited = {}
visited[puzzle] = 0  # 초기 상태의 최단 경로 길이는 0입니다.
q = deque([puzzle])# 큐(queue)를 생성하고 초기 상태를 큐에 넣습니다.

while q:# BFS를 이용하여 8 퍼즐을 풀기 위해 반복합니다.
    b = q.popleft()# 큐의 맨 왼쪽 요소를 빼서 현재 상태를 가져옵니다.
    n = b.find('0')# 현재 상태에서 숫자 0의 위치를 찾습니다.
    x, y = n // 3, n % 3  # 숫자 0의 위치를 좌표 (x, y)로 변환합니다.
    if b == p:# 현재 상태가 목표 상태와 같다면, 즉 8 퍼즐을 모두 풀었다면 반복을 종료합니다.
        break
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:# 이동 가능한 방향은 상하좌우 4가지입니다.
        if nx < 0 or nx == 3 or ny < 0 or ny == 3:# 이동이 범위를 벗어나면 무시하고 다음 방향을 확인합니다.
            continue
        t = b[nx * 3 + ny]# 이동할 위치의 숫자를 가져옵니다.
        temp = b.replace(t, '9').replace('0', t)# 숫자 9가  문자열 0을 반환합니다.
        temp = temp.replace('9', '0')
        if temp not in visited: # 만들어진 다음 상태가 이미 체크한 상태인지 확인합니다.
            q.append(temp)# 이미 체크한 상태가 아니라면 큐에 추가하고 최단 경로 길이를 업데이트합니다.
            visited[temp] = visited[b] + 1
print(visited[p] if p in visited else -1)# 마지막으로 목표 상태 '123456780'의 최단 경로 길이를 출력합니다.
                                    # 만약 목표 상태로 도달할 수 없는 경우 -1을 출력합니다.
