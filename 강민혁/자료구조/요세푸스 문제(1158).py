# 요세푸스 순열
from collections import deque # deque를 이용한 풀이를 위한 선언
N, K = map(int, input().split())


# 방법1. 인덱스를 이용한 코드
'''
people = [i for i in range(1, N+1)]  # 맨 처음 원에 앉아 있는 상태
result = []
n = 0 # 제거될 사람 번호

for i in range(N):
    n += K-1    # 2 4 6 1(8) 3 5 0(7)
    if n >= len(people):
        n = n%len(people)

    result.append(str(people.pop(n)))

print("<",", ".join(result)[:], ">", sep='') 
'''
# 출력이 <3, 6, 2, 7, 5, 1, 4> 이런 식으로 붙어서 출력이 되어야 하기 때문에 sep=''이용

# 방법2. deque를 이용한 풀이
people = deque()
for i in range(1, N+1): # 맨 처음 원에 앉아 있는 상태
    people.append(i)

result = []

while people:
    for _ in range(K-1):
        people.append(people.popleft())

    result.append(people.popleft())

print(str(result).replace('[', '<').replace(']','>'))


'''
초기값 : [1 2 3 4 5 6 7]

<1>
2 3 4 5 6 7 1
3 4 5 6 7 1 2
4 5 6 7 1 2
result = [ 3 ]

<2>
5 6 7 1 2 4
6 7 1 2 4 5
7 1 2 4 5
result = [ 3, 6 ]
'''