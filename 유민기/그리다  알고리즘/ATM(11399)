import sys
n = int(input())  # 사람의 수를 입력받습니다.

person = list(map(int, sys.stdin.readline().split()))  # 각 사람의 수를 리스트로 입력받습니다.
person.sort() # 입력된 값을 오름차순으로 정렬합니다.
result = 0  # 결과를 저장할 변수를 초기화합니다.

for x in range(1, n+1):  # 1부터 n까지의 숫자에 대해 반복합니다.
   result += sum(person[0:x]) # 0부터 x까지의 값을 합하여 result에 누적합니다.
print(result)  # 최종 결과를 출력합니다.
