T = int(input())
for tc in range(1, T + 1):
    st = input()
    stk = []
    for chr in st:
        if not stk:             #비어있으면 push하고
            stk.append(chr)

        else:
            if chr== stk[-1]:   #pop하지않고 읽기만 해서 반복문자이면 pop
                stk.pop()
            else:
                stk.append(chr)  #반복문자가 아니면 push

    print(f'#{tc} {len(stk)}')