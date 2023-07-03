#회의실 배정(1931) 이 문제는 가장 빨리 끝나는 회의 시간으로 오름차순 정렬하여 겹치지 않는 회의들을 정렬된 순서에 따라 카운트 하면 되는 문제이다.
#입력
import sys
N = int(sys.stdin.readline())
time = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time.append([start, end])


#구현
time.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간을 기준으로 오름차순 정렬하되, 끝나는 시간이 같을 경우 시작시간이 빠른 순으로 정렬 

cnt = 0
end = 0
for i in range(N):
    if(end <= time[i][0]): # 끝나는 시간보다 시작하는 시간이 느리거나 같을때
        cnt += 1 # 이 회의를 카운트 해준다
        end = time[i][1] 


#출력
print(cnt)