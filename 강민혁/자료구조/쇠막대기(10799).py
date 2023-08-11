lazor = list(input())
n_stick = 0
stack = []

for i in range(len(lazor)):
    if lazor[i] == '(':  # lazor[i] == '('
        stack.append('(')

    else:  # lazor[i] == ')'
        if lazor[i - 1] == '(':  # 바로 전 stack 데이터가 '('일 때
            stack.pop()
            n_stick += len(stack)

        else:  # 바로 전 stack 데이터가 ')'일 때
            stack.pop()
            n_stick += 1

print(n_stick)

'''
 IDEA

 () 꼴이 만들어 지기 전 몇개의 막대기가 거쳐갔나 확인
 () 꼴이 만들어 지면 길게 이어져 있는 막대를 자른다


'''

