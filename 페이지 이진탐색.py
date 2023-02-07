T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    l = 1
    r = P
    cnt1 = 0
    cnt2 = 0

    while l <= r:
        c = (l + r) //2
        cnt1 += 1
        if c == A:
            break
        elif c!= A:
            if c < A:
                l = c
            elif c > A:
                r = c
    l2=1
    r2=P
    while l2 <= r2:
        c2 = (l2 + r2) //2
        cnt2 += 1
        if c2 == B:
            break
        elif c2!= B:
            if c2 < B:
                l2 = c2
            elif c2 > B:
                r2 = c2

    if cnt1 < cnt2:
        ans = 'A'
    elif cnt1 == cnt2:
        ans = 0
    elif cnt1 > cnt2:
        ans = 'B'

    print(f'#{tc} {ans}')