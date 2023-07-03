#ATM = 이 문제는 운영체제에서 배우는 CPU 스케줄링 중 각 프로세스별 반환 시간(프로세스가 시작해서 끝날때까지 걸리는 시간)이 가장 짧은 스케줄링 방법인 SJF(Shortest Job First) 스케줄링에 대한 문제같다
# 문제에서 요구하는 것 또한 각 사람들이 돈을 인출하는데 걸리는 시간의 최솟값이므로 이를 이용하여서, 돈을 인출하는데 걸리는 시간이 짧은 사람 순서대로 정렬 후, 각 인출 시간을 구하면 최솟값이 나올 것이다.

#입력 및 변수 설정
import sys
N = int(sys.stdin.readline())
withdraws = list(map(int, sys.stdin.readline().split()))
min_sum = 0

#구현
withdraws.sort(key=lambda x: x) # 인출 시간이 빠른 순으로 정렬
temp = 0
for i in range(N):
    temp += withdraws[i] # 한 사람 당 인출 끝나는 시간(대기 시간 + 인출 시간) 
    min_sum += temp # 각 사람들의 시간을 더한다


#출력
print(min_sum)