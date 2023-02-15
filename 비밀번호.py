T = 10
for tc in range(1, T + 1):
    stk = []
    _, st = map(str, input().split())
    for chr in st:
        if not stk:
            stk.append(chr)
        else:
            if chr == stk[-1]:
                stk.pop()
            else:
                stk.append(chr)

    print(f'#{tc} {"".join(stk)}')