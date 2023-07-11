n = int(input())
import sys
input = sys.stdin.readline
arr = [0]
for i in range(n):
    arr.append(int(input()))
dp = [0] * (n+2)

if n <= 2:
    print(sum(arr))
else:
    dp[1] = arr[1]
    dp[2] = max(arr[2], arr[2] + dp[1])
    for i in range(3, n + 1):
        dp[i] = arr[i] + max(dp[i-2], arr[i-1] + dp[i-3])
    print(dp[n])
