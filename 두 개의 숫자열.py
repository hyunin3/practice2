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
        sum = 0
        for j in range(N):
            sum = sum + lst_a[j] * lst_b[i+j]
        if ans < sum:
            ans = sum
        
    print(f'#{tc}', ans)    