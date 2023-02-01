T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    for i in range(N - 1):
        cnt = 0
        for j in range(i + 1, N):
            if lst[i] > lst[j]:
                cnt = cnt + 1
            if ans < cnt:
                ans = cnt

    print(f'#{tc} {ans}')