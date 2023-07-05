# n= 1일때는 1 만 가능 n= 2일때는 00 11만 가능하다 그러면 n=3은 몇개일까? 이는 n=1일때와 n=2일때를 활용하여 유추 가능하다
# n=1일때 1에서 00을 붙여서 만들고 n=2일때의 00, 11들은 1을 붙여서 만든다. 그러면 n=3일때 해당하는 모든 경우의 수가 나올 것이다.
# 우리는 이 규칙을 활용하여 점화식 dp[i] = dp[i-1] + dp[i-2]를 만들 수 있다. 이는 피보나치 함수의 점화식과 동일하다.
N = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])