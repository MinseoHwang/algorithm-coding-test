#회의실 배정
import sys
meeting = int(input())
time_table = [] #회의 시간을 저장한다.

for i in range(meeting):    # 회의 시간을 입력받는다.
    start,end = map(int, sys.stdin.readline().split())
    time_table.append([start,end])

time_table.sort(key = lambda x:x[0]) # 시작시간 기준으로 오름차순 정렬
time_table.sort(key = lambda x:x[1]) # 종료시간 기준으로 오름차순 정렬

max_meeting = 1
# 기준 ( 반복문에서 기준과 각각의 인덱스를 비교해서 그때의 최선을 찾는다)
stn = time_table[0][1]


for i in range(1,meeting):
    if time_table[i][0] > stn: # 기준보다 큰 값을 만났을 때 max_meeting + 1
        max_meeting += 1
        stn = time_table[i][1] # 기준을 최신화 한다.(방금 찾은 인덱스를 기준으로 다시 compare)


print(max_meeting)