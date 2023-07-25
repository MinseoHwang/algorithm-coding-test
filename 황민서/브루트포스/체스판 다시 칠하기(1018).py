n, m = map(int, input().split())
board = []
result = []
 
for _ in range(n):
    board.append(input())

for a in range(n-7):
    for b in range(m-7):
        white = 0
        black = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2==0:
                    if board[i][j]!='W':
                        white +=1
                    else:
                        black +=1
                else:
                    if board[i][j]!='W':
                        black +=1
                    else:
                        white +=1
        result.append(black)
        result.append(white)
print(min(result))

 
