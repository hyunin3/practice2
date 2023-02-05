T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    cnt = [0]*10
    for i in lst:
        cnt[i] += 1
    idx = 0
    for j in range(1,10):
        if cnt[idx]<=cnt[j]:
            idx = j

    print(f'#{tc} {idx} {cnt[idx]}')