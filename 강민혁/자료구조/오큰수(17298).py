'''
A = [3,5,2,7] 인 경우
3의 오른족에 있으면서 3보다 큰 수 중 가장 왼쪽에 있는 원소 5가 오큰수
5의 오른쪽에 있으면서 5보다 큰 수 중 가장 왼쪽에 있는 원소 7이 오큰수
'''
import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        # i가 3일때 Stack에 남아있던 1이 남아 A[1] < A[3] 이 비교되어 answer[1]이 변경된다.
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer) # *answer = answer에 모든 원소들