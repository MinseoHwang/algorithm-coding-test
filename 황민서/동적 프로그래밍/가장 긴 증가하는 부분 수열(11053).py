#입력
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0, 0)
dp = [1] * (n+1)

#구현
for i in range(2, n+1):
    for j in range(1, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)



#출력
print(max(dp))