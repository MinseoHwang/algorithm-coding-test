#괄호를 적절히 쳐서 최솟값을 만드는 문제이다. 처음 -가 나온 시점부터 시작해서 -가 나올때까지 더해준 값을 빼고 이를 반복하면 될 것 같다

#입력 및 변수설정
import sys
input_str = sys.stdin.readline().strip('\n')
plus = input_str.split('-')
num = []

#구현 
for i in plus: # -를 기준으로 나눈 요소들 중 문자열 안에 +가 포함되어 있는 요소들의 덧셈 작업을 위해 for문을 사용하였다.
    temp = i.split('+')
    s = 0
    for j in temp:
        s += int(j)
    num.append(s)
    s = 0
# 30 - 20 + 30 - 10 + 30 일 경우 num의 요소들은 [30, 50, 40]이 될 것이다.


#출력

print(num[0] - sum(num[1:])) # 첫번째 리스트는 양수값이기 때문에 이 값에서 나머지 다 더한 값을 빼준다