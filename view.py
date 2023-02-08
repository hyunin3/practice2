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
    
##############################

#현재 건물의 좌우 4개의 건물 중 가장 큰 값과 현재 건물의 차이를 cnt에 더해준다

T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))  #buildings
    cnt = 0
    for i in range(2, N-2):
        highest = max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
        rls = lst[i] - highest
        if rls > 0:
            cnt += rls
    print(f'#{tc} {cnt}')         
                