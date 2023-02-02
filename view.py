T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    M = 2
    rls = 0
    for i in range(M, N - M):
        mx = lst[i - M]
        for j in range(i - M + 1, i + M + 1):
            if i == j:
                continue
            else:
                if mx < lst[j]:
                    mx = lst[j]
        if lst[i] > mx:
            rls += lst[i] - mx
            
    print(f'#{tc} {rls}')                    