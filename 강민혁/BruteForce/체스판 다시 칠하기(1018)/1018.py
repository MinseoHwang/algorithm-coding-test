# 체스판의 형태가 주어지면 주어진 형태에서 채워주어야 할 체스 칸의 개수를 구하면 된다.
# ex. BWBBBWBW    black과 white가 번갈아가면서 있어야 하지만 B이 연속하여 있다.

# 세로, 가로
n, m = map(int, input().split())
c = []

# 현재 체스판 형태 입력
for i in range(n):  
    chess = input()
    che_ss = list(chess)
    c.append(che_ss)


def repaint(c):
    need_tile = 0
    # 정답지를 만들어 비교
    if (m % 2) != 0:  # 가로가 짝수가 아닐 때
        black = ['B', 'W'] * (m // 2)
        black.append('B')
        white = ['W', 'B'] * (m // 2)
        white.append('W')
    else:  # 가로가 짝수 일 때
        black = ['B', 'W'] * (m // 2)
        white = ['W', 'B'] * (m // 2)

    for i in range(n):
        for j in range(m):
            if (c[0][0] == 'B'):  # 맨 왼쪽 위 칸이 Black인 경우

                if (i % 2) == 0:  # i가 짝수일 때
                    if c[i][j] != black[j]:
                        need_tile += 1
                else:  # i가 홀수 일 때
                    if c[i][j] != white[j]:
                        need_tile += 1
            else:  # 맨 왼쪽 위 칸이 White 인 경우

                if (i % 2) == 0:  # i가 짝수일 때
                    if c[i][j] != white[j]:
                        need_tile += 1
                else:  # i가 홀수 일 때
                    if c[i][j] != black[j]:
                        need_tile += 1
    return need_tile   


print(repaint(c))

'''
IDEA

1. 체스판의 가로 세로 길이를 입력 받는다.
2. 체스판 현 상황을 입력 받는다.
3. 검은 색으로 시작할 때와 흰색으로 시작할때 정답지를 만든다.
4. 무슨 색으로 시작하냐에 따라 정답지를 골라 하나씩 비교한다.(시작색이 Black이면 다음줄 시작은 White가 되어야 한다.)
    4-1) 현재 체스판이 정답지와 다르면 need_tile에 1을 더해준다.
5. need_tile을 출력한다.
'''
