import sys
n = int(input())  # 간격의 개수를 입력받습니다.
time = []  # 간격을 저장할 빈 리스트를 생성합니다.

for i in range(n):   # n번 반복하여 각 간격의 시작 시간과 끝 시간을 입력받습니다.
   start, end = map(int, sys.stdin.readline().split())   # 입력에서 시작 시간과 끝 시간을 읽고 분리합니다.
   time.append([start, end])  # 간격 [시작 시간, 끝 시간]을 time 리스트에 추가합니다.

time = sorted(time, key = lambda x: (x[1], x[0]))  # 간격을 끝 시간을 기준으로 오름차순 정렬하며, 끝 시간이 같은 경우에는 시작 시간을 기준으로 정렬합니다.
            
count = 1  # 호환 가능한 간격의 개수를 추적하기 위한 카운터 변수를 초기화합니다.
last_time = time[0][1]  # 마지막 끝 시간을 저장할 변수를 초기화합니다.
for i in range(1,n):  # 정렬된 간격을 두 번째 간격부터 반복합니다.
   if time[i][0] >= last_time:  # 현재 간격의 시작 시간이 이전 간격의 끝 시간보다 크거나 같은지 확인합니다.
      count += 1  # 만약 크거나 같다면, 호환 가능한 간격이므로 카운터를 증가시킵니다.
      last_time = time[i][1]  # 마지막 끝 시간을 현재 간격의 끝 시간으로 업데이트합니다.
      
print(count)  # 최종 카운트를 출력합니다. 이 값은 호환 가능한 간격의 개수를 나타냅니다.
