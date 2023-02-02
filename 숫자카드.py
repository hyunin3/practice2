T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    cnt = [0]*10
    for n in lst:
        cnt[n] += 1
    idx = 0
    for i in range(1,10):
        if cnt[idx]<=cnt[i]:
            idx = i

    print(f'#{tc} {idx} {cnt[idx]}')