#Knapsack 알고리즘

#물건의 수, 가능 최대 무게 입력
N, K = map(int, input().split())

p = [[0,0]]
kn = [[0]*(K+1) for _ in range(N+1)]

# 물건 정보 입력
for i in range(N):
    p.append(list(map(int, input().split())))

for i in range(1, N+1): # 물건 수
    for j in range(1, K+1): # 물건 무게
        w = p[i][0]
        v = p[i][1]

        if j < w: # 넣을려는 물건 무게가 가능 무게보다 클 때
            kn[i][j] = kn[i-1][j] # 물건을 넣지 않는다
        else:
            # max ( 이전 배낭을 그대로 가지고 감, 이전배낭에서 현재 넣을 무게만큼 배낭에서 빼고 현재 물건을 넣는다.)
            kn[i][j] = max(kn[i-1][j], kn[i-1][j-w] + v)


print(p)
print(kn)
print(kn[N][K])


'''
    SOLUTION
    
    물건을 배낭에 담을 때
    1) 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다
    2) 그렇지 않다면, 다음중 더 나은 가치를 선택하여 넣는다.
      2-1) 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
      2-2) 현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다.
      
      
    입력값  
    4 7         => 물건 개수, 가방 최대 무게 
    6 13        => 무게, 가치
    4 8
    3 6
    5 12
    
    p = [[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]
    kn = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 13, 13], [0, 0, 0, 0, 8, 8, 13, 13], [0, 0, 0, 6, 8, 8, 13, 14], [0, 0, 0, 6, 8, 12, 13, 14]]
                                      1번 물건을 넣었을 때                 2번 물건을 넣었을 때 
    kn[N][K] = 14
'''


