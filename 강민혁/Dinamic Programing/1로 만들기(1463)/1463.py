#입력
N = int(input())

dp = [0,0,1,1]

if N < 4:   # 입력이 4보다 작을 때
    print(dp[N])

else:    #입력이 3보다 클때
    for i in range(4,N+1):

        sol1 = 1 + dp[i-1]
        sol2 = 1 + dp[i-1]
        sol3 = 1 + dp[i-1]

# i가 2로 나누어 지면 dp[i//2]에서 계산이 한번 더 되었기 때문에 1 더한 값이 sol2값이 된다.
# i가 3으로 나누어 지는 경우도 같다.
        
        if (i % 2) == 0:
            sol2 = 1 + dp[i//2]
        if (i % 3) == 0:
            sol3 = 1 + dp[i//3]

        dp.append(min(sol1,sol2,sol3))
    
    #출력
    print(dp[N])



