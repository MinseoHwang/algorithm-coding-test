#입력
n = int(input())

dp = [0] * 1000001   # List 초기화 부분: 입력받는 N+1의 크기를 갖게 한다.

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746     #점화식

#출력
print(dp[n])

