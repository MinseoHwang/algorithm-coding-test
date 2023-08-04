import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start):
    queue = deque()
    queue.append(start)
    moved = dict()
    moved[start] = 0

    while queue:
        state = queue.popleft()

        if state == "123456780":
            return moved[state]

        now_idx = state.find("0")
        x = now_idx // 3
        y = now_idx % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or 3 <= nx or 0 > ny or 3 <= ny:
                continue
                
            next_idx = nx * 3 + ny # 문자열 리스트의 현재 인덱스로 변환하는 작업
            next_num = list(state) # 문자열을 리스트로 변환
            next_num[next_idx], next_num[now_idx] = next_num[now_idx], next_num[next_idx] #자리 바꾸기
            next_num = "".join(next_num) # 다시 문자열로 변환

            if not moved.get(next_num):
                queue.append(next_num)
                moved[next_num] = moved[state] + 1
    
    return -1

start = ""
for _ in range(3):
    temp = sys.stdin.readline().strip()
    temp = temp.replace(" ", "")
    start += temp

print(bfs(start))






