# 대표적인 냅색 문제라고 한다. 
#바텀업 방식으로 풀었으며, 점화식은 dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])이다
# luggage[i][0]은 무게, luggage[i][1]은 가치이다
#입력
import sys
n, k = map(int, sys.stdin.readline().split())

luggage = [[0, 0]]
for i in range(1, n + 1):
    w, v = map(int, sys.stdin.readline().split())
    luggage.append([w, v])

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if (luggage[i][0] <= j):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-luggage[i][0]] + luggage[i][1])
        else:
            dp[i][j] = dp[i-1][j]


print(dp[n][k])