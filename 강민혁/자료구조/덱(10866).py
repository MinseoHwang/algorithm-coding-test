from collections import deque
import sys

N = int(input())
dq = deque()
output = []

for _ in range(N):
    com = input()   # 입력

    if "push_front" in com:    # push_front
        com, a = com.split()
        a = int(a)
        dq.appendleft(a)

    elif "push_back" in com:    # push_back
        com, a = com.split()
        a = int(a)
        dq.append(a)

    elif com == "pop_front":    # pop_front
        if len(dq) == 0:
            output.append(-1)
        else:
            output.append(dq.popleft())

    elif com == "pop_back":    # pop_back
        if len(dq) == 0:
            output.append(-1)
        else:
            output.append(dq.pop())

    elif com == "size":    # size
        output.append(len(dq))

    elif com == "empty":    # empty
        if len(dq) == 0:
            output.append(1)
        else:
            output.append(0)

    elif com == "front":    # front
        if len(dq) == 0:
            output.append(-1)
        else:
            output.append(dq[0])

    elif com == "back":    # back
        if len(dq) == 0:
            output.append(-1)
        else:
            output.append(dq[-1])

# 출력 부분 최적화
print('\n'.join(map(str, output))[:], end='')
