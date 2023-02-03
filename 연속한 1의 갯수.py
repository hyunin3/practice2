T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    cnt = 0
    ans = 0
    for i in range(N):
        if lst[i] == 0:
            cnt = 0
        elif lst[i] ==1:
            cnt = cnt + 1
            if ans < cnt:
                ans = cnt

    print(f'#{tc}', ans)