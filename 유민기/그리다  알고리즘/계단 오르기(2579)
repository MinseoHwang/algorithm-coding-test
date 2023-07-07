import sys
input = sys.stdin.readline

n = int(input())  # 입력받을 계단의 수

dp = [0] * (n + 1)  # 계단의 최댓값을 저장할 DP 테이블
p = [0] * (n + 1)  # 계단의 점수를 저장할 p 배열

# 각 계단의 점수를 입력받음
for i in range(1, n + 1):
    p[i] = int(input())

if n == 1:  # 계단이 1개일 경우 해당 계단의 점수를 출력
    print(p[1])
    exit()
elif n == 2:  # 계단이 2개일 경우 첫 번째 계단과 두 번째 계단의 점수를 더한 값을 출력
    print(sum(p[:3]))
    exit()

dp[1] = p[1]  # 첫 번째 계단의 점수는 그대로 저장
dp[2] = p[1] + p[2]  # 두 번째 계단의 점수는 첫 번째 계단과 두 번째 계단의 점수를 더한 값으로 저장

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + p[i], dp[i - 3] + p[i - 1] + p[i])  # i번째 계단의 점수는 (i-2번째 계단의 점수 + i번째 계단의 점수)와 (i-3번째 계단의 점수 + i-1번째 계단의 점수 + i번째 계단의 점수) 중에서 최댓값을 선택하여 저장

print(dp[i]) # 계단 수가 n일 때의 최댓값 출력
