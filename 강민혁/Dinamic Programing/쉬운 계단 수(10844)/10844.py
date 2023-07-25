# 입력
N = int(input())

# dp[i][j]: i 자리수에서 j로 끝나는 계단 수의 개수
dp = [[0] * 10 for _ in range(N + 1)]

# 한 자리 수일 때 , 모든 수는 계단 수
for i in range(1, 10):
    dp[1][i] = 1

# 두 자리 수부터 n 자리 수까지 계단 수 개수 계산
for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

# 출력
print(sum(dp[N]) % 1000000000)
