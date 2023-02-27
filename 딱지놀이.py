N = int(input())
for _ in range(N):
    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))
    #print(lsta[0], lstb[0])
    star1 = cir1 = tan1 = tri1 = 0
    for i in lsta[1:]:
        if i == 4:
            star1 += 1
        if i == 3:
            cir1 += 1
        if i == 2:
            tan1 += 1
        if i == 1:
            tri1 += 1
    star2 = cir2 = tan2 = tri2 = 0
    for i in lstb[1:]:
        if i == 4:
            star2 += 1
        if i == 3:
            cir2 += 1
        if i == 2:
            tan2 += 1
        if i == 1:
            tri2 += 1
    #print(star1, cir1, tan1, tri1)
    if star1 > star2:
        ans = 'A'
    elif star1 < star2:
        ans = 'B'
    else:
        if cir1 > cir2:
            ans = 'A'
        elif cir1 < cir2:
            ans = 'B'
        else:
            if tan1 > tan2:
                ans = 'A'
            elif tan1 < tan2:
                ans = 'B'
            else:
                if tri1 > tri2:
                    ans = 'A'
                elif tri1 < tri2:
                    ans = 'B'
                else:
                    ans = 'D'
    print(ans)
