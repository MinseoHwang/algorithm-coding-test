#입력
import sys
n = int(input())

line = [[0, 0]] 
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    line.append([start, end])
dp = [1] * (n+1)

#구현
line.sort(key=lambda x: x[0])

for i in range(2, n+1):
    for j in range(1, i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

#출력
print(n - max(dp))
