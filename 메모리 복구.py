T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input()))
    N = len(lst)
    cnt = 0
    for i in range(N-1):
        if lst[i] != lst[i + 1]:
            cnt += 1
    if lst[0] == 0:
        pass
    elif lst[0] == 1:
        cnt +=1

    print(f'#{tc} {cnt}')