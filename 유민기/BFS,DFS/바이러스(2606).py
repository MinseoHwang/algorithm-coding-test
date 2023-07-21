#바이러스 2606
"""https://www.acmicpc.net/problem/2606"""
import sys

input = sys.stdin.readline

# 깊이 우선 탐색(DFS) 로 풀어보기
# DFS : 스택 사용 , 스택에 담는 순서가 중요, 방문 순서대로 스택에 담는다. 스택은 list로 표현 ( 후입 선출 ), 재귀로 사용 가능??
# 번호가 낮은 인접노드부터 방문
'''
예시에 나온 그림을 기준으로 하면
1 - 2 - 3 - 5 - 6  //  4 - 7
이런 순으로 방문하게 된다.
'''
n = int(input())
c = int(input())

# 그래프 만들기
# 비어있는 이중 배열리스트를 생성.
# 인덱스를 해당하는 컴퓨터의 번호와 매칭해야 하므로 범위는 n개에서 1개 더 추가해야 함
# (그래야 0~n까지 나오므로)
graph = [[] for i in range(n+1)]

# 방문한 번호 확인하기 위한 리스트(스택) 생성
# 이 방문 리스트조차 존재하는 컴퓨터 대수만큼 인덱스와 매칭해야 하므로 n+1개만큼 생성
# 또한 방문했으면 해당 인덱스번호에 True로 바꿔서 방문했는지 확인할 예정
visited = [False] * (n+1)

# visited의 True 개수 확인하면 되지 않을까?
for _ in range(c):
    # a = 로컬 컴퓨터 , b = 연결된 컴퓨터
    # 방향이 지정되지 않았기 때문에 양방향으로 연결이 가능
    # graph에 양쪽으로 담아주기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# print(graph)

def dfs(graph, now_visit, visited):
    # 방문한 번호 확인하는 리스트의 현재 방문한 번호가 True이면
    # 현재 방문한 번호를 출력한다.
    visited[now_visit] = True
    # 1번과 연결된 방문한 컴퓨터 숫자 출력됨
    # print(now_visit)
    
    # 여기서 출력하면 아래 재귀에 걸리는 것까지 다 출력됨
    # print(sum(visited)-1)
    
    # 그래프의 현재 방문한 숫자의 인덱스 안에 들어있는 인수들
    # 인수들은 그 인덱스와 일치하는 컴퓨터와 연결된 컴퓨터의 숫자이다.
    # 그 숫자들이 i에 담겨서 반복되는데,
    # 방문한 적이 없는 숫자인 경우
    # dfs 함수에 다시 넣어서(재귀함수) i를 now_visit로 삼아서 돌린다.
    for i in graph[now_visit]:
        if not visited[i]: # if not visited[index] 는 visited[index]==False 와 동일하다
            dfs(graph, i, visited)
    
    # 여기서 출력하면 마지막 함수 종료된 것만 출력됨
    return sum(visited)-1

# 문제에서 1번 컴퓨터와 연결된 컴퓨터를 찾아달라고 했으니
# now_visit는 1로 입력해서 넣어준다.
print(dfs(graph, 1, visited))
