T = 10
for tc in range(1, T + 1):
    N = int(input())
    st = input()
    stk = []
    equ = ''
    cal = []
    for chr in st:
        if not stk and chr == '+':
            stk.append(chr)
        elif stk and chr == '+':
            equ += stk.pop()
            stk.append(chr)
        else:
            equ += chr
    else:
        equ += stk.pop()                

    
    for chr in equ:
        if chr != '+':
            cal.append(int(chr))
        elif chr == '+':
            n2 = cal.pop()
            n1 = cal.pop()
            cal.append(n1 + n2)

    print(f'#{tc}', *cal)        
