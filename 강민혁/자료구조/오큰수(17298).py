'''
A = [3,5,2,7] 인 경우
3의 오른족에 있으면서 3보다 큰 수 중 가장 왼쪽에 있는 원소 5가 오큰수
5의 오른쪽에 있으면서 5보다 큰 수 중 가장 왼쪽에 있는 원소 7이 오큰수
'''

N = int(input())
A = list(map(int,input().split())) # 수열 입력
Stack = []
Answer = []

for i in range(N):
    for j in range(i+1,N):
        if A[i] < A[j]:     # 오른쪽에서 큰수
            Stack.append(A[j])

    if Stack:   # Stack이 비어있지 않으면
        Answer.append(Stack[0])
    else:           # Stack이 비어있을 때
        Answer.append(-1)
    Stack.clear()

print(" ".join(map(str,Answer))[:])