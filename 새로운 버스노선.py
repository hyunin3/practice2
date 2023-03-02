T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * 1001
    ans = 0
    for _ in range(N):
        B, s, e = map(int, input().split())
        if B == 1:
            for i in range(s, e+1):
                cnt[i] += 1
        elif B == 2:
            for i in range(s, e, 2):
                cnt[i] += 1
            cnt[e] += 1
        elif B == 3:
            if s % 2 == 0:
                for i in range(s+1, e):
                    if i % 4 == 0:
                        cnt[i] += 1
                cnt[s] += 1
                cnt[e] += 1
            else:
                for i in range(s+1, e):
                    if i % 3 == 0 and i % 10 != 0:
                        cnt[i] += 1
                cnt[s] += 1
                cnt[e] += 1

    for n in cnt:
        if ans < n:
            ans = n

    print(f'#{tc} {ans}')