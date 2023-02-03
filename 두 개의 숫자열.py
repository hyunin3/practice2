T = int(input())
for tc in range(1, T + 1):
    N, M = map(int(input().split()))
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))
    
    if len(lst_a) > len(lst_b):
        lst_a, lst_b = lst_b, lst_a
        N, M = M, N
    ans = -1000000
    
    for i in range(M-N+1):
        cnt = 0
        for j in range(N):
            cnt = cnt + lst_a[i] * lst_b[i+j]
        if ans < cnt:
            ans = cnt
        
    print(f'#{tc}', ans)    