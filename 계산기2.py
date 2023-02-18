pri = {'+': 1, '*': 2}
T = 10
for tc in range(1, T + 1):
    N = int(input())
    st = input()

    # [1] 후위표기식으로 변환
    # 숫자: equ추가, 연산자: stk[-1]에서 나보다 우선순위 높은(같은경우도 높음)
    # 연산자 모두 pop해서 equ추가 후 지금 연산자 push
    equ = ""
    stk = []
    for chr in st:
        if chr.isdigit():
            equ += chr
        else:
            while stk and pri[chr] <= pri[stk[-1]]:
                equ += stk.pop()
            # 후위표기식: 연산자는 일단 push되고 연산할 대상숫자 뒤에 위치!!! (항상)
            stk.append(chr)
    # 스택사용시: 동작완료후 스택에 남아있는 데이터 처리!! (오류 이거나 미완료)
    while stk:
        equ += stk.pop()

    # [2] 후위표기식 연산!
    # 숫자면 push, 연산자면 stk에서 2개 pop (순서주의!!!) 연산 => 결과를 push
    for chr in equ:
        if chr.isdigit():
            stk.append(int(chr))
        elif chr == '+':
                stk.append(stk.pop() + stk.pop())
                
        elif chr == '*':
                stk.append(stk.pop() * stk.pop())        

    ans = stk.pop()
    print(f'#{tc} {ans}')